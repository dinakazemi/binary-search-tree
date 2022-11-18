import unittest
import range_size_tree

def first_test():
        T = range_size_tree.RangeSizeTree()
        T.put(1)
        assert (T.get(1)[0].get_key() == 1)
        assert (len(T.get(1)) == 1)
        assert (T.range_size(1,1) == 1)
        assert (T.range_size(3,2) == 0)
        assert (T.remove(3) == None)
        assert (T.remove(1).get_key() == 1)
def second_test():
        T = range_size_tree.RangeSizeTree()
        assert (T.get(4) == [])
        assert (T.remove(3) == None)
        assert (T.range_size(0,4) == 0)
def third_test():
        T = range_size_tree.RangeSizeTree()
        T.put(10)
        T.put(7)
        T.put(7)
        T.put(5)
        T.put(3)
        T.put(3)
        T.put(3)
        T.put(2)
        T.put(0)
        assert(len(T.get(3)) == 3 and len(T.get(7)) == 2)
        assert(T.remove(1) == None)
        assert(T.remove(3).get_parent().get_key() == 3)
        assert(len(T.get(3)) == 2)
        assert(T.range_size(2,7) == T.range_size(7,2))
        assert(T.range_size(2,7) == 6)
        T.remove(10)
def fourth_test():
        T = range_size_tree.RangeSizeTree()
        T.put(3)
        T.put(6)
        T.put(7)
        T.put(9)
        T.put(10)
        T.put(15)
        assert (T.remove(2) == None)
        assert(T.range_size(3,15) == 6)
        T.remove(6)
        assert(T.root.get_key() == 3)
        assert(T.root.get_right().get_key() == 7)
        T.remove(3)
        assert(T.root.get_key() == 7)
def fifth_test():
        T = range_size_tree.RangeSizeTree()
        T.put(3)
        T.put(5)
        T.put(3)
        T.put(0)
        T.put(4)
        T.put(4)
        T.put(4)
        T.put(4.5)
        T.put(3.5)
        T.print_tree('l')
        print("---")
        assert(len(T.get(4)) == 3)
        assert(T.range_size(3,4) == 6)
        T.remove(4)
        assert(T.range_size(3,4) == 5)
        T.print_tree('l')
        print("---")
        T.remove(4)
        T.print_tree('l')
        print("---")
        T.remove(3)
        T.print_tree('l')
        print("---")
        T.remove(3)
        assert(T.root.get_key() == 3.5)
        T.print_tree('l')
        
if __name__ == '__main__':
        first_test()
        second_test()
        third_test()
        fourth_test()
        fifth_test()
        print ("all tests passed")