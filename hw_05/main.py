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

def get_tokens_from_file(file_path):
    file_path = cwd() + file_path
    file_text = open(file_path).read()
    all_tokens = nltk.word_tokenize(file_text)

    return all_tokens

def remove_bad_tokens(tokens):
    relevant_tokens = [token for token in tokens \
        if not token in closed_class_stop_words \
        and token not in string.punctuation \
        and not token.isdigit()
        and token not in headers]

    return relevant_tokens

def initialize_query_dictionary(query_file):
    query_dictionary = {}

    for line in query_file:
        line_token = nltk.word_tokenize(line)
        if line_token[0] == ".I":
            query_id = line_token[1]
        else:
            prev_query_text = query_dictionary.get(query_id) or ''
            query_text = prev_query_text + line
            query_dictionary.update({query_id: query_text})

    return query_dictionary

def tokenize_query_dictionary(query_dictionary):
    for query_id in query_dictionary:
        query_text = query_dictionary.get(query_id)
        query_tokens = nltk.word_tokenize(query_text)
        query_dictionary[query_id] = query_tokens

    return query_dictionary

def clean_query_dictionary(query_dictionary):
    for query_id in query_dictionary:
        query_tokens = query_dictionary.get(query_id)
        cleaned_tokens = remove_bad_tokens(query_tokens)
        query_dictionary[query_id] = cleaned_tokens

    return query_dictionary

def make_query_dictionary(query_file):
    query_dictionary = initialize_query_dictionary(query_file)
    tokenized_query_dictionary = tokenize_query_dictionary(query_dictionary)
    cleaned_query_dictionary = clean_query_dictionary(tokenized_query_dictionary)

    return cleaned_query_dictionary

if __name__ == "__main__":
    query_file = open(cwd() + 'cran/cran.qry')
    query_dictionary = make_query_dictionary(query_file)
    number_of_queries = len(query_dictionary)

    print query_dictionary
    print number_of_queries






