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

def calculate_idf(collection_size, term_frequency_in_collection):
    idf = collection_size/term_frequency_in_collection
    return log(idf)

def make_query_dictionary(query_file):
    """
    Given a File object, creates a dictionary of the form
    {'query_id': ['token_1': token_1_freq, 'token_2': token_2_freq,... 'token_n': token_n_freq}
    where all stop words, punctuation, and numbers are removed.
    """
    query_dict = {}

    # initialize dict with values as raw strings
    for line in query_file:
        line_token = nltk.word_tokenize(line)
        if line_token[0] == ".I":
            query_id = line_token[1]
        else:
            prev_query_text = query_dict.get(query_id) or ''
            query_text = prev_query_text + line
            query_dict.update({query_id: query_text})

    # tokenize the dict values and add per-query token frequency
    for query_id in query_dict:
        query_text = query_dict.get(query_id)
        query_tokens = nltk.word_tokenize(query_text)
        query_tokens = remove_bad_tokens(query_tokens)
        tokens_with_frequencies = add_term_frequencies(query_tokens)
        query_dict.update({query_id: tokens_with_frequencies})

    query_file.seek(0)  # return to start of file

    return query_dict

def make_abstract_dictionary(abstract_file):
    """
    Given a File object, creates a dictionary of the form
    {'abstract_id': ['token_1': token_1_freq, 'token_2': token_2_freq,... 'token_n': token_n_freq}
    where all stop words, punctuation, and numbers are removed.
    """
    abstract_dict = {}
    concat_flag = False

    # initialize dict with values as raw strings
    for line in abstract_file:
        line_token = nltk.word_tokenize(line)
        if line_token[0] in headers:
            if line_token[0] == ".I":
                abstract_id = line_token[1]
            elif line_token[0] == ".W":
                concat_flag = True
            else:
                concat_flag = False
        else:
            if concat_flag:
                prev_line = abstract_dict.get(abstract_id) or ''
                abstract_text = prev_line + line
                abstract_dict.update({abstract_id: abstract_text})

    # tokenize the dict values and add per-abstract token frequency
    for abs_id in abstract_dict:
        abstract_text = abstract_dict.get(abs_id)
        abstract_tokens = nltk.word_tokenize(abstract_text)
        abstract_tokens = remove_bad_tokens(abstract_tokens)
        tokens_with_frequencies = add_term_frequencies(abstract_tokens)
        abstract_dict.update({abs_id: tokens_with_frequencies})

    abstract_file.seek(0)  # return to start of file

    return abstract_dict

def count_docs_containing_term(collection, token):
    doc_count = 0

    for doc_id in collection:
        doc_dict = collection.get(doc_id)  # returns {'token_1': token_1_tf, 'token_2':...}
        unique_tokens_of_doc = list(set(doc_dict.keys()))
        if token in unique_tokens_of_doc:
            doc_count += 1

    return doc_count

def get_unique_tokens(doc_dict):
    all_tokens = []

    for doc_id in doc_dict:
        doc_tokens = doc_dict.get(doc_id)
        for key in doc_tokens:
            all_tokens.append(key)

    unique_tokens = list(set(all_tokens))
    return unique_tokens


def make_idf_dictionary(doc_dict):
    """ Given a File object, creates a dictionary of the form
    {'token': inverse_document_frequency}
    """

    tokens = get_unique_tokens(doc_dict)
    idf_dict = {}
    collection_size = len(doc_dict)

    idf_dict = {token: calculate_idf(collection_size,
        count_docs_containing_term(doc_dict, token))
        for token in tokens}

    return idf_dict

def make_query_feature_vectors(query_dict, token_dict):
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

if __name__ == "__main__":
    query_file = open(cwd() + 'cran/cran.qry')
    query_dict = make_query_dictionary(query_file)
    token_dict = make_token_dictionary(query_file, query_dict)

    query_feature_vectors = make_query_feature_vectors(query_dict, token_dict)

    print query_feature_vectors

