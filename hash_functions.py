""" Python module containing hash functions
"""

import random


def h_ascii(key, N):
    """ Basic hash function using ASCII values of characters. takes a string
    key and a hash table size and returns a hash that is based on the sum of
    the ASCII values for the characters in the key.

    Parameters
    ----------
    key - A key used to store data in a hash table. This hash function
    requires that key is a string.

    N - the size of the hash table array

    Returns
    -------
    An integer corresponding to the position in the hash table the key, value
    will be stored
    """

    s = 0
    try:
        for i in range(len(key)):
            s += ord(key[i])
    except TypeError:
        print('key for ascii hash function must be a string')
    return s % N


def h_rolling(key, N, p=53, m=2**64):
    """ A hash function using the polynomial rolling hash algorithm. p a prime
     number roughly equal to the number of characters in the input alphabet.
     m should be a large number, since the probability of two random strings
     colliding is about 1/m. Sometimes m=2^64 is chosen.

    Parameters
    ----------
    key - A key used to store data in a hash table. This hash function
    requires that key is a string.

    N - the size of the hash table array

    p - a prime number roughly equal to the number of characters in the input
    alphabet

    m - a large number

    Returns
    -------
    An integer corresponding to the position in the hash table where key, value
    will be stored
    """

    s = 0
    try:
        for i in range(len(key)):
            s += ord(key[i]) * p**i
        s = s % m
    except TypeError:
        print('key for rolling hash function must be a string')
    return s % N


def h_python(key, N):
    """ Python's built in hash function

    Parameters
    ----------
    key - A key used to store data in a hash table. This hash function
    requires that key is a string.

    N - the size of the hash table array

    Returns
    -------
    An integer corresponding to the position in the hash table the key, value
    will be stored
    """
    return hash(key) % N
