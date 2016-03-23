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

if __name__ == "__main__":
    all_query_tokens = get_tokens_from_file('cran/cran.qry')
    query_tokens = remove_bad_tokens(all_query_tokens)

    print query_tokens


