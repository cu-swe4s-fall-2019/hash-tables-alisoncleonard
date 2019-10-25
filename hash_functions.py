""" Python module containing hash functions
"""

import random
import argparse


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


def main():
    """
    Main function allows calling hash function from the command line.

    Parameters
    ----------
    key_file_name - a txt file containing string keys to hash

    hash_function - the hash function to call. Either ascii, rolling, or python

    Returns
    -------
    A list of hash slots for each key in key_file
    """
    parser = argparse.ArgumentParser(description='Implement hash functions',
                                     prog='hash_functions.py')

    parser.add_argument('key_file_name', type=str, help='txt file containing '
                        'keys for hash function')

    parser.add_argument('hash_function', type=str, help='hash algorithm. '
                        "choose from 'ascii', 'rolling', or 'python' from "
                        'hash_functions.py')

    args = parser.parse_args()

    key_file = args.key_file_name
    hash_alg = args.hash_function

    key_list = []
    f = open(key_file, 'r')
    for line in f:
        y = line.split()
        key_list.append(y)

    for key in key_list:
        if hash_alg == 'ascii':
            print(h_ascii(str(key), (len(key_list) + 1)))
        if hash_alg == 'rolling':
            print(h_rolling(str(key), (len(key_list) + 1)))
        if hash_alg == 'python':
            print(h_python(str(key), (len(key_list) + 1)))


if __name__ == '__main__':
    main()
