import re
import unittest

import main

class TestMain(unittest.TestCase):

    def test_remove_stop_words(self):
        tokens = ['.I', '365', '.W', 'what', 'design', 'factors', 'can', 'be', 'used', 'to', 'control', 'lift-drag', 'ratios', 'at', 'mach', 'numbers', 'above', '5', '.']
        expected_tokens = ['.I', '365', '.W', 'design', 'factors', 'used', 'control', 'lift-drag', 'ratios', 'mach', 'numbers', '5', '.']

        filtered_tokens = main.remove_stop_words(tokens)

        self.assertEqual(filtered_tokens, expected_tokens)

    def test_remove_numbers(self):
        original_tokens = ['.I', '087', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']
        expected_tokens = ['.I', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']

        filtered_tokens = main.remove_numbers(original_tokens)

        self.assertEqual(filtered_tokens, expected_tokens)

    def test_remove_punctuation(self):
        original_tokens = ['.I', '087', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']
        expected_tokens = ['.I', '087', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', 'the', 'slip', 'effect',]

        filtered_tokens = main.remove_punctuation(original_tokens)

        self.assertEqual(filtered_tokens, expected_tokens)

    def test_remove_headers(self):
        original_tokens = ['.I', '087', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']
        expected_tokens = ['087', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']

        filtered_tokens = main.remove_headers(original_tokens)

        self.assertEqual(filtered_tokens, expected_tokens)


