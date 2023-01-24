import unittest

from indexation.indexation import *

class TestIndexation(unittest.TestCase):

    def test_tokenize(self):
        string = 'Catholicisme — Wikipédia'
        actual = tokenize(string)
        expected = ['Catholicisme', '—', 'Wikipédia']
        self.assertEqual(actual, expected)
    
    def test_word_frequency(self):
        tokens = ['Catholicisme', '—', 'Wikipédia']
        actual = word_frequency(tokens)
        expected = {'Catholicisme': 1, '—': 1, 'Wikipédia': 1}
        self.assertEqual(dict(actual), expected)
    
    def test_created_inverted_index(self):
        list_token = [['a', 'b', 'b'], ['a', 'b','c']]
        actual = create_inverted_index(list_token)
        expected = [{'a': ['1:1', '0:1'], 'b': ['0:2', '1:1'], 'c': ['1:1']},
                    {'a': ['1:1', '0:1'], 'b': ['1:1', '0:2'], 'c': ['1:1']},
                    {'a': ['0:1', '1:1'], 'b': ['0:2', '1:1'], 'c': ['1:1']},
                    {'a': ['0:1', '1:1'], 'b': ['1:1', '0:2'], 'c': ['1:1']}]
        self.assertIn(dict(actual), expected)