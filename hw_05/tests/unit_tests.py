import re
import unittest

import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.query_test_file = open('tests/query_test_file.qry')
        self.test_tokens_short = ['.I', '087', '.W', 'what', 'is', 'the', 'available', 'information', 'pertaining', 'to', 'the', 'effect', 'of', 'slight', 'rarefaction', 'on', 'boundary', 'layer', 'flows', '(', 'the', '?', 'slip', '?', 'effect', ')', '.']
        self.test_tokens_long = ['.I', '15', '.T', 'on', 'two-dimensional', 'panel', 'flutter', '.', '.A', 'fung', ',', 'y.c', '.', '.B', 'j.', 'ae', '.', 'scs', '.', '25', ',', '1958', ',', '145', '.', '.W', 'on', 'two-dimensional', 'panel', 'flutter', '.', 'theory', 'and', 'experiments', 'of', 'the', 'flutter', 'of', 'a', 'buckled', 'plate', 'are', 'discussed', '.', 'it', 'is', 'shown', 'that', 'an', 'increase', 'in', 'the', 'initial', 'deviation', 'from', 'flatness', 'or', 'a', 'static', 'pressure', 'differential', 'across', 'the', 'plate', 'raises', 'the', 'critical', 'value', 'of', 'the', '/reduced', 'velocity', './', 'the', 'applicability', 'of', 'the', 'galerkin', 'method', 'to', 'the', 'linearized', 'problem', 'of', 'flutter', 'of', 'an', 'unbuckled', 'plate', 'has', 'been', 'questioned', 'by', 'several', 'authors', '.', 'in', 'this', 'paper', 'the', 'flutter', 'condition', 'was', 'formulated', 'in', 'the', 'form', 'of', 'an', 'integral', 'equation', 'and', 'solved', 'numerically', 'by', 'the', 'method', 'of', 'iteration', 'and', 'the', 'method', 'of', 'matrix', 'approximations', ',', 'thus', 'avoiding', 'the', 'constraint', 'of', 'assumed', 'modes', '.', 'for', 'a', 'plate', '(', 'with', 'finite', 'bending', 'rigidity', ')', 'the', 'results', 'confirm', 'those', 'given', 'by', 'the', 'galerkin', 'method', '.', 'an', 'approximate', 'analysis', 'of', 'the', 'limiting', 'form', 'and', 'amplitude', 'of', 'the', 'flutter', 'motion', 'for', 'a', 'buckled', 'plate', 'is', 'presented', '.', '.I', '16', '.T', 'transformation', 'of', 'the', 'compressible', 'turbulent', 'boundary', 'layer', '.', '.A', 'mager', ',', 'a', '.', '.B', 'j.', 'ae', '.', 'scs', '.', '25', ',', '1958', ',', '305', '.', '.W', 'transformation', 'of', 'the', 'compressible', 'turbulent', 'boundary', 'layer', '.', 'the', 'transformation', 'of', 'the', 'compressible', 'turbulent', 'boundary-', 'layer', 'equations', 'to', 'their', 'incompressible', 'equivalent', 'is', 'demonstrated', 'analytically', '.', 'the', 'transformation', 'is', 'essentially', 'the', 'same', 'as', 'that', 'for', 'the', 'laminar', 'layer', ',', 'first', 'given', 'by', 'stewartson', ',', 'except', 'that', 'the', 'explicit', 'relation', 'between', 'the', 'viscosity', 'and', 'temperature', 'is', 'not', 'required', '.', 'a', 'key', 'point', 'in', 'the', 'analysis', 'is', 'the', 'modification', 'of', 'the', 'stream', 'function', 'to', 'include', 'a', 'mean', 'of', 'the', 'fluctuating', 'components', 'and', 'the', 'postulate', 'that', 'the', 'apparent', 'turbulent', 'shear', ',', 'associated', 'with', 'an', 'elemental', 'mass', ',', 'remains', 'invariant', 'in', 'the', 'transformation', '.', 'the', 'values', 'of', 'the', 'incompressible', 'friction', 'coefficients', 'and', 'of', 'pressure', 'rise', 'causing', 'separation', 'thus', 'transformed', 'show', 'good', 'agreement', 'with', 'the', 'experimentally', 'measured', 'and', 'independently', 'reported', 'results', '.', 'anreported', 'results', '.', 'anreported', 'results', '.', 'anreporeserving', 'boundary', 'layers', 'and', 'to', 'the', 'computations', 'of', 'general', 'boundary-layer', 'flow', 'is', 'shown', '.']

    def test_remove_bad_tokens(self):
        original_tokens = self.test_tokens_short
        expected_tokens = ['available', 'information', 'pertaining', 'effect', 'slight', 'rarefaction', 'boundary', 'layer', 'flows', 'slip', 'effect']

        filtered_tokens = main.remove_bad_tokens(original_tokens)

        self.assertEqual(filtered_tokens, expected_tokens)

    def test_make_query_dictionary(self):
        query_dictionary = main.make_query_dictionary(self.query_test_file)

        expected_dictionary = {'041':['progress', 'made', 'research', 'unsteady', 'aerodynamics'],
                               '049':['factors', 'influence', 'time', 'required', 'invert', 'large', 'structural', 'matrices'],
                               '050':['does', 'practical', 'flow', 'follow', 'theoretical', 'concepts', 'interaction', 'between', 'adjacent', 'blade', 'rows', 'supersonic', 'cascade']}

        self.assertEqual(query_dictionary, expected_dictionary)



