import re
import unittest

import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.query_test_file = open('tests/query_test_file.qry')
        self.test_tokens_short = ['.I', '087', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']

    def test_remove_bad_tokens(self):
        original_tokens = self.test_tokens_short
        expected_tokens = ['available', 'information', 'pertaining', 'effect', 'slight', 'rarefaction', 'boundary', 'layer', 'flows', 'slip', 'effect']

        filtered_tokens = main.remove_bad_tokens(original_tokens)

        self.assertListEqual(filtered_tokens, expected_tokens)

    def test_make_query_dictionary(self):
        query_dict = main.make_query_dictionary(self.query_test_file)

        expected_dict = {'041':['progress', 'made', 'research', 'unsteady', 'aerodynamics'],
                               '049':['factors', 'influence', 'time', 'required', 'invert', 'large', 'structural', 'matrices'],
                               '050':['does', 'practical', 'flow', 'follow', 'theoretical', 'concepts', 'interaction', 'between', 'adjacent', 'blade', 'rows', 'supersonic', 'cascade']}

        self.assertDictEqual(query_dict, expected_dict)



