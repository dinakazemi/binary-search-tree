import node
import tree_interface

class RangeSizeTree(tree_interface.RSTreeInterface):
        """
        Range Size Tree

        Implements the Range Size Tree interface.
        Supports insertion, removal and getting the node.
        """

        def __init__(self):
                """
                Initialise the tree, root node is none.
                """
                self.root = None

        def put(self, k):
                """
                Put the value K into the tree.

                Hint McHintFace: watch out for duplicates!
                :param k: The key to insert into the tree.
                """
                def helper(u):
                        u.increment_subtree()
                       # print (u.get_key(),u._subtree_size)
                        if (k<=u.get_key()):
                                if (u.get_left() == None):
                                        new_node = node.Node(k)
                                        new_node.set_parent(u)
                                        u.set_left(new_node)
                                        #self.root.increment_subtree()
                                        return
                                helper(u.get_left())
                        elif (k>u.get_key()):
                                if (u.get_right() == None):
                                        new_node = node.Node(k)
                                        new_node.set_parent(u)
                                        u.set_right(new_node)
                                        
                                        return
                                helper(u.get_right())
                if (self.root == None):
                        self.root = node.Node((k))
                else:
                        helper(self.root)

        def get(self, k):
                """
                Get the node(s) with key `k`.

                E.g.
                      3
                   /     \
                  1       5
                 / \     / \
                1   2   4   6


                get(1) => returns array of both 1 (parent 1), 1 (parent 3)
                NOTE: ordered LEFT TO RIGHT!

                :param k: The key to get.
                :return: Array of Node's with key K.
                """
                result = []
                def helper(u):
                        if (u == None):
                                return result
                        if (u.get_key() == k):
                                result.append(u)
                                if (u.get_left() != None):
                                        helper(u.get_left())
                                else:
                                        return result
                        elif (u.get_key()>k):
                                if (u.get_left()!=None):
                                        helper(u.get_left())
                                else:
                                        return result
                        elif (u.get_key()<k):
                                if (u.get_right()!=None):
                                        helper(u.get_right())
                                else:
                                        return result
                helper(self.root)
                return result[::-1]

        def remove(self, k):
                """
                Remove's the value from the tree.

                Note: with duplicates, find the "FIRST DEEPEST OCCURRENCE"

                E.g.
                      3
                   /     \
                  1       5
                 / \     / \
                1   2   4   6

                Remove (1)

                      3
                   /     \
                  1       5
                   \     / \
                    2   4   6

                :param k: value to remove from the tree.
                :return: The removed Node. None if node not found OR cannot be removed.
                """
                output = []
                def helper(u):
                        if (u == None):
                                return output
                        u.decrement_subtree()
                        if (u.get_key() == k):
                                output.append(u)
                                if (u.get_left() != None):
                                        helper(u.get_left())
                                else:
                                        return output
                        elif (u.get_key()>k):
                                if (u.get_left()!=None):
                                        helper(u.get_left())
                                else:
                                        return output
                        elif (u.get_key()<k):
                                if (u.get_right()!=None):
                                        helper(u.get_right())
                                else:
                                        return output
                helper(self.root)
                if (output == []):
                        return None
                result = output[-1]
                if (result.get_left() != None and result.get_right()!=None):
                        result_copy = result
                        n = result.get_right()
                        while (n.get_left()!=None):
                                n = n.get_left()
                        result.set_key(n.get_key())
                        result.get_left().set_parent(result)
                        result.get_right().set_parent(result)
                        n.get_parent().set_left(None)

                        return result_copy
                if (result.get_left() == None or result.get_right() == None):
                        #are we removing the root?
                        if (result.get_parent() == None):
                                if (result.get_left() == None and result.get_right() == None):
                                        self.root = None
                                elif (result.get_left()!=None):
                                        result.get_left().set_parent(None)
                                        self.root = result.get_left()
                                elif (result.get_right() != None):
                                        result.get_right().set_parent(None)
                                        self.root = result.get_right()
                                return result
                        #check which child our result is?
                        if (result == result.get_parent().get_left()):
                                #if it is the left child:
                                if (result.get_left() == None and result.get_right() == None):
                                        #if both left and right child of result are none
                                        result.get_parent().set_left(None)
                                        return result
                                elif (result.get_left() == None):
                                        #if only left child is none
                                        result.get_parent().set_left(result.get_right())
                                        result.get_right().set_parent(result.get_parent())
                                        return result
                                else:
                                        #if only right child is none
                                        result.get_parent().set_left(result.get_left())
                                        result.get_left().set_parent(result.get_parent())
                                        return result
                        else:
                                if (result.get_left() == None and result.get_right() == None):
                                        #if both left and right child of result are none
                                        result.get_parent().set_right(None)
                                        return result
                                elif (result.get_left() == None):
                                        #if only left child is none
                                        result.get_parent().set_right(result.get_right())
                                        result.get_right().set_parent(result.get_parent())
                                        return result
                                else:
                                        #if only right child is none
                                        result.get_parent().set_left(result.get_left())
                                        result.get_left().set_parent(result.get_parent())
                                        return result   
        def range_size(self, a, b):
                """
                Calculates the size between two keys.
                (Inclusive!)

                e.g.
                  2
                 / \
                1  3

                range_size(1, 1) => 1

                e.g. #2
                            5
                        /       \
                      3          7
                    /   \      /   \
                  2      4    6     8
                 / \     \        /  \
                1   3     5      8   10

                range_size(3, 7) => 7

                :param a: A key to search between.
                :param b: A key to search between.
                :return: Number of nodes between the two keys.
                """
                result = [0]
                if (a<=b):
                        min = a
                        max = b
                else:
                        min = b
                        max = a
                def helper(u, result):
                        #print (u.get_key(), result[0])
                        if (u == None):
                                return result
                        if (u.get_key()>max):
                                #print("too big, going to the left node")
                                if (u.get_left() == None):
                                        #print (result[0])
                                        return result
                                helper(u.get_left(),result)
                        if (u.get_key()<min):
                                #print("too small, going to the rigt node")
                                if (u.get_right() == None):
                                        #print (result[0])
                                        return result
                                helper(u.get_right(),result)
                        if (min<u.get_key() and max>u.get_key()):
                                #print ("in the range")
                                result[0]+=1
                                if (u.get_right() == None and u.get_left() == None):
                                        #print (result[0])
                                        return result
                                if (u.get_left()!=None):
                                        helper(u.get_left(),result)
                                if (u.get_right()!=None):
                                        helper(u.get_right(),result)
                        if (min == u.get_key()):
                                #print ("equal to min, going to the left and right node")
                                result[0]+=1

                                if (u.get_left()==None and u.get_right() == None):
                                        #print (result[0])
                                        return result
                                if (u.get_left()!=None):
                                        helper(u.get_left(),result)
                                if (u.get_right()!=None):
                                        helper(u.get_right(),result)
                        if (min!=max):
                                if (max == u.get_key()):
                                        #print ("equal to max, going to the left node")
                                        result[0]+=1
                                        #print (result[0])
                                        if (u.get_left() == None):
                                                #print (result[0])
                                                return result
                                        helper(u.get_left(),result)
                helper(self.root,result)
                return result[0]
                      
        def print_tree(self,s):
                key =  str(self.root.get_key())
                if (self.root.get_parent() == None):
                        parent = 'None'
                else:    
                        parent = str(self.root.get_parent().get_key())
                if (s == 'r'):
                        print ("node " + key + " is a right child of " + parent)
                else:    
                        print ("node " + key + " is a left child of " + parent)
                if (self.root.get_left() != None):
                        #print (key + " has a left child.")
                        t = RangeSizeTree()
                        t.root = self.root.get_left()
                        t.print_tree('l')
                if (self.root.get_right() != None):
                        t = RangeSizeTree()
                        t.root = self.root.get_right()
                        t.print_tree('r')

################################################################################
# The following functions are not tested
# They are provided for you to run and test.
################################################################################

def main():
        T = RangeSizeTree()
        T.put(1)
        T.put(2)
        n = T.range_size(2,1)
        print (n)
        # T.put(1.5)
        T.print_tree('l')
        # result = T.get(1.5)
        # for i in range(0,len(result)):
        #         print (result[i].get_parent().get_key(),result[i].get_key())
        # root_str = str(T.root.get_key())
        # print ("Root is equalt to: " + root_str)
        # removed_node = T.remove(1)
        # print(removed_node.get_key())
        # T.print_tree('l')


if __name__ == "__main__":
        print("Running main method of RangeSizeTree")
        main()
