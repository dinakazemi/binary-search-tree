"""
Simple Binary Tree Node to be used in the Binary Tree.
"""


class Node:
        """
        Simple node in the binary tree.
        """

        def __init__(self, key):
                self._key = key
                self._subtree_size = 1
                self._left = None
                self._right = None
                self._parent = None

        def get_key(self):
                """
                Returns the value of the node's key

                :return: the node key
                """
                return self._key

        def get_subtree_size(self):
                """
                Returns size of the subtree below this node.

                :return: size of the subtree
                """
                return self._subtree_size

        def increment_subtree(self):
                """
                Increments the size of the subtree.
                """
                self._subtree_size += 1

        def decrement_subtree(self):
                """
                Decrement the size of the subtree.
                """

                if self._subtree_size == 1:
                        return

                self._subtree_size -= 1

        def get_left(self):
                """
                Get the left child

                :return: Left child node
                """
                return self._left

        def get_right(self):
                """
                Get the right child

                :return: Right child node
                """
                return self._right

        def get_parent(self):
                """
                Get the parent of the node.

                :return: The parent.
                """
                return self._parent

        def set_left(self, l):
                """
                Set the left child of the node.
                """
                self._left = l


        def set_right(self, r):
                """
                Set the right child of the node.
                """
                self._right = r


        def set_parent(self, p):
                """
                Set the parent.
                """

                self._parent = p
        def set_key(self,k):
                """
                changes the key.
                """
                self._key = k
