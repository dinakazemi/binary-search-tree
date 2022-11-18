"""
Range Size Tree Interface
(Pretty much a binary tree)

Provides a simple interface that will be used in the assessment.
Will outline what methods must exist in the implemented tree.
"""

import abc


class RSTreeInterface(metaclass=abc.ABCMeta):
        """
        RSTree Interface.
        Implements the put, remove and get functions of a tree.
        Supports the "range size" function which finds the number of nodes between two given
        keys.
        """

        @abc.abstractmethod
        def put(self, k):
                """
                Place `k` into the tree
                :param k: The key to place into the tree.
                """
                pass

        @abc.abstractmethod
        def remove(self, k):
                """
                Remove `k` from the tree.
                :param k: The key to remove from the tree.
                """
                pass

        @abc.abstractmethod
        def get(self, k):
                """
                Returns the node(s) with the key K
                :param k: the value to search for.
                :return: the node with key `k`.
                """
                pass

        @abc.abstractmethod
        def range_size(self, a, b):
                """
                Get the number of nodes between two values
                :param a: a value
                :param b: a value
                :return: The number of nodes.
                """
                pass
