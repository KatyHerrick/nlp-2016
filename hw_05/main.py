# Katy Herrick
# NLP Homework #5 - Ad Hoc Information Retrieval
# 3/21/16

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

def make_query_dictionary(query_file):
    """
    Given a File object, creates a dictionary of the form
    {'query_id': ['token_1', 'token_2',... 'token_n'}
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

    # tokenize the dict values
    for query_id in query_dict:
        query_text = query_dict.get(query_id)
        query_tokens = nltk.word_tokenize(query_text)
        query_tokens = remove_bad_tokens(query_tokens)
        query_dict[query_id] = query_tokens

    query_file.seek(0)  # return to start of file

    return query_dict

def make_token_dictionary(query_file, query_dict):
    """ Given a File object, creates a dictionary of the form
    {'token': number_of_queries_token_appears_in}
    """
    token_frequency_dict = {}

    file_text = query_file.read()
    tokens = nltk.word_tokenize(file_text)
    unique_tokens = set(remove_bad_tokens(tokens))

    for unique_token in unique_tokens:
        for query_id in query_dict:
            query = query_dict.get(query_id)
            for token in query:
                if token == unique_token:
                    prev_frequency = token_frequency_dict.get(unique_token) or 0
                    token_frequency = prev_frequency + 1
                    token_frequency_dict.update({unique_token: token_frequency})

    query_file.seek(0)  # return to start of file

    return token_frequency_dict






