import re
import unittest

import main
from stop_list import closed_class_stop_words, headers
from string import punctuation

class TestMain(unittest.TestCase):

    maxDiff = None

    def test_remove_bad_tokens(self):
        original_tokens = ['.I', '087', '.W', 'what', 'is', 'the', 'available', \
            'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', \
            'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', \
            'slip', '?', 'effect', ')', '.', '5', 'thousand']
        expected_tokens = ['available', 'information', 'pertaining', 'effect', \
            'slight', 'rarefaction', 'boundary', 'layer', 'flows', 'slip', \
            'effect', 'thousand']

        filtered_tokens = main.remove_bad_tokens(original_tokens)

        self.assertListEqual(filtered_tokens, expected_tokens, "Tokens should not \
            contain numbers, punctuation, or stop words.")

    def test_parse_keys_match_doc_ids(self):
        with open('tests/query_test_file.qry') as test_file:
            abstract_parses = main.parse(test_file)

        expected_keys = ['041', '049', '050']
        self.assertEqual(set(expected_keys), set(abstract_parses.keys()))

    def test_parse_ignores_titles_authors_and_bibs(self):
        with open('tests/abstracts_test_file.txt') as test_file:
            abstract_parses = main.parse(test_file)

        expected_text_of_ab_5 = "one-dimensional transient heat conduction into a double-layer\nslab subjected to a linear heat input for a small time\ninternal ."

        self.assertEqual(abstract_parses.get('5'), expected_text_of_ab_5,
            "Text should not contain author or bibliographic information.")

    def test_tf_dict_values_contain_correct_tokens(self):
        with open('tests/query_test_file.qry') as test_file:
            tf_dict = main.make_tf_dictionary(test_file)

        expected_tokens = ['supersonic', 'rows', 'concepts', 'flow', \
        'theoretical', 'large', 'cascade', 'interaction', 'does', 'adjacent', \
        'between', 'follow', 'blade', 'practical']
        tokens_of_query_050 = tf_dict.get('050').keys()
        self.assertEqual(set(tokens_of_query_050), set(expected_tokens))

    def test_tf_dict_values_contain_correct_freqs(self):
        with open('tests/query_test_file.qry') as test_file:
            tf_dict = main.make_tf_dictionary(test_file)

        tokens_of_query_050 = ['supersonic', 'rows', 'concepts', 'flow', \
        'theoretical', 'large', 'cascade', 'interaction', 'does', 'adjacent', \
        'between', 'follow', 'blade', 'practical']

        freqs_of_query_050 = tf_dict.get('050').values()