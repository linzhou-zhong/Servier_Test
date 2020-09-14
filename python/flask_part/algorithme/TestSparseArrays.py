import unittest
from SparseArrays import *

_strings = ['abc', 'ab', 'ac']  # Strings
_queries = ['abc', 'ab']  # Queries
_result = {'ab': 1, 'abc': 1}  # Expected Result
_sa = SparseArrays(strings=_strings, queries=_queries)  # Test class


class TestSparseArrays(unittest.TestCase):
    # Test of Brute Force method
    def test_count_frequency_brute_force(self):
        self.assertEqual(_sa.count_frequency_brute_force(), _result)

    # Test of inner function List.count()
    def test_count_frequency_inner_func(self):
        self.assertEqual(_sa.count_frequency_inner_func(), _result)

    # Test of Optimized method
    def test_count_frequency_optimization(self):
        self.assertEqual(_sa.count_frequency_optimization(), _result)


if __name__ == '__main__':
    unittest.main()
