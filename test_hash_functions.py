""" Unit test file for hash_functions.py module
"""

import unittest
import hash_functions


class TestHashFunctions(unittest.TestCase):

    def test_ascii_constant_key(self):
        k = 107
        e = 101
        y = 121
        ascii_total = k + e + y
        N = 20
        self.assertEqual(hash_functions.h_ascii('key', 20), ascii_total % N)

    def test_ascii_key_not_string(self):
        key = 8
        N = 20
        self.assertRaises(TypeError, hash_functions.h_ascii(key, N))

    def test_rolling_constant_key(self):
        k = 107 * 53**0
        e = 101 * 53**1
        y = 121 * 53**2
        s = (k + e + y) % (2**64)
        N = 20
        p = hash_functions.h_rolling('key', 20, p=53, m=2**64)
        q = s % N
        self.assertEqual(p, q)

    def test_rolling_key_not_string(self):
        key = 17
        N = 20
        self.assertRaises(TypeError, hash_functions.h_rolling(key, N))

    def test_divide_by_random_key_not_string(self):
        key = 4
        N = 20
        self.assertRaises(TypeError, hash_functions.h_rolling(key, N))


if __name__ == '__main__':
    unittest.main()
