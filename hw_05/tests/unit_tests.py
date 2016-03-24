import re
import unittest

import main

class TestMain(unittest.TestCase):

    maxDiff = None

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

        expected_dict = {'041': {'made': 1, 'aerodynamics': 1, 'research': 1, 'large': 1, 'progress': 1, 'unsteady': 1},
        '049': {'factors': 1, 'invert': 1, 'required': 1, 'influence': 1, 'large': 1, 'time': 2, 'structural': 1, 'matrices': 1, 'unsteady': 1},
        '050': {'large': 1, 'interaction': 1, 'rows': 1, 'supersonic': 1, 'between': 1, 'flow': 1, 'practical': 1, 'cascade': 1, 'does': 1, 'adjacent': 1, 'concepts': 1, 'follow': 3, 'blade': 1, 'theoretical': 1}
        }

        self.assertDictEqual(query_dict, expected_dict)

    def test_count_queries_containing_term(self):
        query_dict = main.make_query_dictionary(self.query_test_file)
        query_count = main.count_queries_containing_term(query_dict, "follow")
        expected_query_count = 1

        self.assertEqual(query_count, expected_query_count)

    def test_make_token_dictionary(self):
        query_dict = main.make_query_dictionary(self.query_test_file)
        token_dict = main.make_token_dictionary(self.query_test_file, query_dict)

        expected_dict = {'blade': 1.0986122886681098, 'aerodynamics': 1.0986122886681098, 'influence': 1.0986122886681098, 'follow': 1.0986122886681098, 'large': 0.0, 'rows': 1.0986122886681098, 'factors': 1.0986122886681098, 'invert': 1.0986122886681098, 'research': 1.0986122886681098, 'does': 1.0986122886681098, 'adjacent': 1.0986122886681098, 'between': 1.0986122886681098, 'progress': 1.0986122886681098, 'theoretical': 1.0986122886681098, 'concepts': 1.0986122886681098, 'interaction': 1.0986122886681098, 'matrices': 1.0986122886681098, 'structural': 1.0986122886681098, 'supersonic': 1.0986122886681098, 'made': 1.0986122886681098, 'required': 1.0986122886681098, 'flow': 1.0986122886681098, 'practical': 1.0986122886681098, 'cascade': 1.0986122886681098, 'time': 1.0986122886681098, 'unsteady': 0.4054651081081644}

        self.assertDictEqual(token_dict, expected_dict)

