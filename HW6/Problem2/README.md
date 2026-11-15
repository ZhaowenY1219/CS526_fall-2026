================================================================================
README.md - Problem 2
================================================================================


--------------------------------------------------------------------------------
 Introduction 
--------------------------------------------------------------------------------



--------------------------------------------------------------------------------
 Algorithm
--------------------------------------------------------------------------------

step 1 Define the Node ADT
--------------------------------------------------------------------------------
Create a Node ADT to represent each individual node in the binary heap, and each node must following below conditions:

1. 'value': stores the value held by the current node
2. 'left':stroes a reference to the left child node. if no left child exists, set it to 'None':left = None
3. 'right':stroes a reference to the right child node. if no right child exists, set it to 'None':right = None
4. 'parent':stroes a reference to the parent node. if no parent exists, set it to 'None':parent = None

When creating a new node, initialize its values ​​with the given input, and set its left, right, and parent references to 'None'

when connecting nodes to form the binary tree, update the references between the parent node and its children. FOr example,

           root_node.left = left_node   # set the parent's left reference to point to the left child
           root_node.right = right_node # set the parent's right reference to point to the right child

           left_node.parent = root_node  # set the left child's parent reference to point back to the parent node
           right_mode.parent = root_node # set the right child's parent reference to point back to the parent node

step 2 Define the Heap ADT
--------------------------------------------------------------------------------
Create a Min- Heap ADT to manage the entire binary heap, and the heap must maintain the following conditions:
1. 'root': stores a reference to the root node of the heap. if heap is empty, set it to 'None': self.root = None
2. 'size': stores  the current number of nodes in the heap. initialize to '0'

when the heap is initialized, set 'root' to 'None' and 'size' to '0'

The heap must maintain the following conditions after every operation:
1. each parent node's value must be less than or equal to their children's value
2. every level must be full except the last level, which must be filled from left to right
3. each node's parent,lef,right reference must correctly represent its position in the tree
4. update the size whenever a node is successfully inserted or removed
