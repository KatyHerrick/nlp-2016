# Katy Herrick
# NLP Homework #5 - Ad Hoc Information Retrieval
# 3/21/16

from __future__ import division
from math import log
import nltk
import os.path
import string
import re

from stop_list import closed_class_stop_words, headers

def cwd():
    return os.path.dirname(os.path.dirname(__file__))

def remove_bad_tokens(tokens):
    relevant_tokens = [token for token in tokens \
        if not token in closed_class_stop_words \
        and token not in string.punctuation \
        and not token.isdigit()
        and token not in headers]

    return relevant_tokens

def add_term_frequencies(tokens):
    return {token: tokens.count(token) for token in tokens}

def make_tf_dictionary(collection_file):
    """
    Given a File object, creates a dictionary of the form
    {'abstract/query_id': ['token_1': token_1_freq, 'token_2': token_2_freq,... 'token_n': token_n_freq}
    where all stop words, punctuation, and numbers are removed.
    """
    collection = {}
    concat_flag = False

    # initialize dict with values as raw strings
    for line in collection_file:
        line_token = nltk.word_tokenize(line)
        if line_token[0] in headers:
            if line_token[0] == ".I":
                doc_id = line_token[1]
            elif line_token[0] == ".W":
                concat_flag = True
            else:
                concat_flag = False
        else:
            if concat_flag:
                prev_line = collection.get(doc_id) or ''
                doc_text = prev_line + line
                collection.update({doc_id: doc_text})

    # tokenize the dict values and add per-doc token frequency
    for doc_id in collection:
        doc_text = collection.get(doc_id)
        doc_tokens = nltk.word_tokenize(doc_text)
        doc_tokens = remove_bad_tokens(doc_tokens)
        tokens_with_frequencies = add_term_frequencies(doc_tokens)
        collection.update({doc_id: tokens_with_frequencies})

    return collection

def count_docs_containing_term(collection, token):
    doc_count = 0

    for doc_id in collection:
        doc_dict = collection.get(doc_id)
        unique_tokens_of_doc = list(set(doc_dict.keys()))
        if token in unique_tokens_of_doc:
            doc_count += 1

    return doc_count

def get_unique_tokens(collection_dict):
    all_tokens = []
    for doc_id in collection_dict:
        doc_tokens = collection_dict.get(doc_id)
        for key in doc_tokens:
            all_tokens.append(key)

    return list(set(all_tokens))

def calculate_idf(collection_size, term_frequency_in_collection):
    return log(collection_size/term_frequency_in_collection)

def make_idf_dictionary(per_doc_tf_dict):
    """ Given a dictionary of documents with per-document term frequencies,
    returns a dictionary of the form
    {'token': inverse_document_frequency}
    """
    tokens = get_unique_tokens(per_doc_tf_dict)
    idf_dict = {}
    collection_size = len(per_doc_tf_dict)

    idf_dict = {token: calculate_idf(collection_size,
        count_docs_containing_term(per_doc_tf_dict, token))
        for token in tokens}

    return idf_dict

def make_query_vectors(query_dict, token_dict):
    """ Returns a dictionary of the form
    {'001': ['term_1': term_1_idf, 'term_2': term_2_idf,... 'term_x': term_x_idf]
    '002': ['term_1': term_1_idf, 'term_2': term_2_idf,... 'term_y': term_y_idf], ...
    ['query_id_n:  ['term_1': term_1_idf, 'term_2': term_2_idf,... 'term_z': term_z_idf]
    """
    query_feature_vectors = {}

    for query_id in query_dict:
        query = query_dict.get(query_id)
        term_tf_idf_scores = {}

        for token in query:
            tf = query.get(token)
            idf = token_dict.get(token)
            term_tf_idf_scores.update({token: tf*idf})

        query_feature_vectors.update({query_id: term_tf_idf_scores})

    return query_feature_vectors

def make_abstract_vector(query_vector, abstract_tfs, abstract_idfs):
    token_tf_idf_scores = {}
    for token in query_vector.keys():
        tf = abstract_tfs.get(token) or 0.0
        idf = abstract_idfs.get(token) or 0.0
        token_tf_idf_scores.update({token: tf*idf})

    return token_tf_idf_scores

def make_vectors_for_single_query(query_vector, abstract_tfs_lookup, abstract_idfs):
    abstract_vectors_for_single_query = {}
    for abstract_id in abstract_tfs_lookup.keys():
        abstract_tfs = abstract_tfs_lookup.get(abstract_id)
        abstract_vector = make_abstract_vector(query_vector, abstract_tfs, abstract_idfs)
        abstract_vectors_for_single_query.update({abstract_id: abstract_vector})

def make_abstract_vectors_by_query(query_vectors, abstract_tfs_lookup, abstract_idfs):
    abstract_vectors = {}

    for query_id in query_vectors:
        query_vector = query_vectors.get(query_id)
        abs_vectors_for_this_query = make_vectors_for_single_query(query_vector, abstract_tfs_lookup, abstract_idfs)
        abstract_vectors.update({query_id: abs_vectors_for_this_query})

    return abstract_vectors

if __name__ == "__main__":
    query_file = open(cwd() + 'cran/cran.qry')
    per_query_tfs = make_tf_dictionary(query_file)

    abstract_file = open(cwd() + 'cran/cran.all.1400')
    per_abstract_tfs = make_tf_dictionary(abstract_file)

    query_term_idfs = make_idf_dictionary(per_query_tfs)
    abstract_term_idfs = make_idf_dictionary(per_abstract_tfs)

    query_vectors = make_query_vectors(per_query_tfs, query_term_idfs)
    abstract_vectors = make_abstract_vectors_by_query( \
        query_vectors, per_abstract_tfs, abstract_term_idfs)

