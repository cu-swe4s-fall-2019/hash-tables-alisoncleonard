"""Hash_tables.py creates classes containing hash tables using different
collision resolution strategies. Main functions tests performance of hash
functions and collision reduction strategies in hash tables.
"""

import hash_functions
import argparse
import time
import random
import sys


class LinearProbe:
    """Hash table using linear probing collision resolution strategy
    """
    def __init__(self, N, hash_function):
        """Initialize hash table

        Parameters
        ----------
        N - size of hash table array
        hash_function - hash function from hash_functions.py module

        Returns
        -------
        self.hash - hash function object
        self.N - size of hash table object
        self.T - hash table object of size self.N
        self.M - number of keys object
        """
        self.hash = hash_function
        # N = size of table
        self.N = N
        # creates hash table T
        self.T = [None for i in range(N)]
        # M = number of keys
        self.M = 0

    def add(self, key, value):
        """Add keys and values to hash table

        Parameters
        ----------
        key - key to search hash table
        value - value corresponding to a set key

        Returns
        -------
        If there is space in the table, adds key, value pair to self.T,
        increases self.M by 1, returns True
        If the hash table is full, returns False
        """
        start_hash = self.hash(key, self.N)
        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        """Searches for key in hash table

        Parameters
        ----------
        key - key to search hash table

        Returns
        -------
        If key is in hash table, returns associated value
        If key is not in hash table, returns None
        """
        hash_slot = self.hash(key, self.N)
        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainedHash:
    """Hash table using chained hash collision resolution strategy
    """
    def __init__(self, N, hash_function):
        """Initialize hash table

        Parameters
        ----------
        N - size of hash table array
        hash_function - hash function from hash_functions.py module

        Returns
        -------
        self.hash - hash function object
        self.N - size of hash table object
        self.T - hash table object of size self.N
        self.M - number of keys object
        """
        self.hash = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0
        self.keys = []

    def add(self, key, value):
        """Add keys and values to hash table

        Parameters
        ----------
        key - key to search hash table
        value - value corresponding to a set key

        Returns
        -------
        Adds key, value pair to hash table. Returns True
        """
        if self.search(key) == None:
            start_hash = self.hash(key, self.N)
            self.T[start_hash].append((key, value))
            self.M += 1
            self.keys.append(key.strip('\n'))
        return True

    def search(self, key):
        """Searches for key in hash table

        Parameters
        ----------
        key - key to search hash table

        Returns
        -------
        If key is in hash table, returns associated value
        If key is not in hash table, returns None
        """
        hash_slot = self.hash(key, self.N)
        for k, v in self.T[hash_slot]:
            if key == k:
                return v
        return None

def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val

def main():
    """
    use hash table classes to build functional tables. benchmark performance
    of different hash functions and collision resolution strategies
    """

    parser = argparse.ArgumentParser(description='Build hash tables and '
                                     'benchmark performance',
                                     prog='hash_tables.py')

    parser.add_argument('table_size', type=int, help='Size of hash table')

    parser.add_argument('hash_alg', type=str, help='hash algorithm. '
                        "choose from 'ascii', 'rolling', or 'python' from "
                        'hash_functions.py')

    parser.add_argument('coll_strtgy', type=str, help='hash table class'
                        "choose from 'linear' or 'chain' classes")

    parser.add_argument('data_file', help='input data file')

    parser.add_argument('num_keys', type=int, help='number of keys to hash')


    args = parser.parse_args()

    N = args.table_size
    hash_alg = args.hash_alg
    collision_strategy = args.coll_strtgy
    data_file_name = args.data_file
    keys_to_add = args.num_keys

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_ascii)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_ascii)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_rolling)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_rolling)

    elif hash_alg == 'python':
        if collision_strategy == 'linear':
            ht = LinearProbe(N, hash_functions.h_python)
        elif collision_strategy == 'chain':
            ht = ChainedHash(N, hash_functions.h_python)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('add', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)


if __name__ == '__main__':
    main()
