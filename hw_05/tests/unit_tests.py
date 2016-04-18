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



    # def test_make_tf_dictionary(self):

    #     query_dict = main.make_tf_dictionary(self.query_test_file)

    #     expected_dict = {'041': {'made': 1, 'aerodynamics': 1, 'research': 1, 'large': 1, 'progress': 1, 'unsteady': 1},
    #     '049': {'factors': 1, 'invert': 1, 'required': 1, 'influence': 1, 'large': 1, 'time': 2, 'structural': 1, 'matrices': 1, 'unsteady': 1},
    #     '050': {'large': 1, 'interaction': 1, 'rows': 1, 'supersonic': 1, 'between': 1, 'flow': 1, 'practical': 1, 'cascade': 1, 'does': 1, 'adjacent': 1, 'concepts': 1, 'follow': 3, 'blade': 1, 'theoretical': 1}
    #     }

    #     self.assertDictEqual(query_dict, expected_dict)

    def xtest_count_docs_containing_term(self):
        # improve this with trickier data
        query_dict = main.make_tf_dictionary(self.query_test_file)
        query_count = main.count_docs_containing_term(query_dict, "follow")
        expected_query_count = 1

        self.assertEqual(query_count, expected_query_count)

    def test_calculate_idf(self):
        pass

    def test_idf_dict_contains_all_unique_tokens(self):
        pass

    def test_idf_dict_contains_correct_idfs(self):
        pass

    # def test_make_idf_dictionary(self):
    #     query_dict = main.make_tf_dictionary(self.query_test_file)
    #     token_dict = main.make_idf_dictionary(query_dict)

    #     expected_dict = {'blade': 1.0986122886681098, 'aerodynamics': 1.0986122886681098, 'influence': 1.0986122886681098, 'follow': 1.0986122886681098, 'large': 0.0, 'rows': 1.0986122886681098, 'factors': 1.0986122886681098, 'invert': 1.0986122886681098, 'research': 1.0986122886681098, 'does': 1.0986122886681098, 'adjacent': 1.0986122886681098, 'between': 1.0986122886681098, 'progress': 1.0986122886681098, 'theoretical': 1.0986122886681098, 'concepts': 1.0986122886681098, 'interaction': 1.0986122886681098, 'matrices': 1.0986122886681098, 'structural': 1.0986122886681098, 'supersonic': 1.0986122886681098, 'made': 1.0986122886681098, 'required': 1.0986122886681098, 'flow': 1.0986122886681098, 'practical': 1.0986122886681098, 'cascade': 1.0986122886681098, 'time': 1.0986122886681098, 'unsteady': 0.4054651081081644}

    #     self.assertDictEqual(token_dict, expected_dict)

    def test_make_query_vectors_has_all_ids(self):
        pass

    #def test_make_query_vectors_

    def test_make_abstract_feature_vectors_by_query(self):
        pass
