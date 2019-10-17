"""
Unit tests for hash_tables.py
"""

import unittest
import hash_tables
import hash_functions
import random


class TestHashFunctions(unittest.TestCase):

    def testLinearProbe_add_to_empty_ascii(self):
        x = random.randint(0, 100)
        y = hash_functions.h_ascii
        test = hash_tables.LinearProbe(x, y)
        self.assertTrue(test.add('key', 10))

    def testLinearProbe_add_to_full_ascii(self):
        x = random.randint(0, 100)
        y = hash_functions.h_ascii
        test = hash_tables.LinearProbe(x, y)
        test.T = [str(random.randint(0, 100)) for i in range(test.N)]
        self.assertFalse(test.add('key', 10))

    def testLinearProbe_search_not_in_table_ascii(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_ascii)
        test.T = [str(random.randint(0, 100)) for i in range(test.N)]
        self.assertFalse(test.search('key'))

    def testLinearProbe_search_in_table_ascii(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_ascii)
        test.T = [(str(i), 2*i) for i in range(test.N)]
        self.assertEqual(test.search('3'), 6)

    def testLinearProbe_search_in_table_rolling(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_rolling)
        test.T = [(str(i), 2*i) for i in range(test.N)]
        self.assertEqual(test.search('3'), 6)

    def testLinearProbe_search_in_table_python(self):
        test = hash_tables.LinearProbe(10, hash_functions.h_python)
        test.T = [(str(i), 2*i) for i in range(test.N)]
        self.assertEqual(test.search('3'), 6)

    def testChainedHash_add_to_empty_ascii(self):
        x = random.randint(0, 100)
        y = hash_functions.h_ascii
        test = hash_tables.ChainedHash(x, y)
        self.assertTrue(test.add('key', 10))

    def testChainedHash_search_not_in_table_ascii(self):
        test = hash_tables.ChainedHash(10, hash_functions.h_ascii)
        self.assertFalse(test.search('key'))

    def testChainedHash_search_in_table_ascii(self):
        test = hash_tables.ChainedHash(10, hash_functions.h_ascii)
        for i in range(5):
            test.add(str(i), 2*i)
        self.assertEqual(test.search('3'), 6)

    def testChainedHash_search_in_table_rolling(self):
        test = hash_tables.ChainedHash(10, hash_functions.h_rolling)
        for i in range(5):
            test.add(str(i), 2*i)
        self.assertEqual(test.search('3'), 6)

    def testChainedHash_search_in_table_python(self):
        test = hash_tables.ChainedHash(10, hash_functions.h_python)
        for i in range(5):
            test.add(str(i), 2*i)
        self.assertEqual(test.search('3'), 6)


if __name__ == '__main__':
    unittest.main()
