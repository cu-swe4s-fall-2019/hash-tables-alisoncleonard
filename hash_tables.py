"""Hash_tables.py creates classes containing hash tables using different
collision resolution strategies
"""

import hash_functions


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
        start_hash = self.hash(key, self.N)
        self.T[start_hash].append((key, value))
        self.M += 1
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
