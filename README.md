# binary-search-tree
This repo implements a Binary Search Tree.  
The Range Size Tree supports this functionality: 
- `put(k)` - put the key K into the tree (duplicate keys are allowed).
- `remove(k)` - remove the lowest occurrence of the key K.
- `get(k)` - return the nodes that have the key K.
- `size(a, b)` - count the number of nodes between a and b. 
    - NOTE: a and b may not be in order; may not be a key etc.
    - If a < lowest tree node, you should still count from this.
    - Similarly if b > highest tree node, still count between this.

Descendants to the LEFT are LESS THAN OR EQUAL TO ( <= ) the node's value.  
Descendants to the RIGHT are STRICTLY GREATER THAN ( > ) the node's value.

## How to run the program?

Make sure you first create and customise your tree in the `main` method of `range_size_tree.py`, and then run `python3 range_size_tree.py`.
