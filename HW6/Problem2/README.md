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

The heap ADT needs to implement the following operations:
insert(value)
peek()
extract_min()
delete(value)
build(values)
heap_sort()
is_empty()
__len__() len(heap)
print_heap()

step 3 Define insert(value)
--------------------------------------------------------------------------------
The insert(value) uses the next available position to maintain the complete shape of the binary heap, which followed by bubbling up to restore the heap order

1. check whether the heap is empty. if it is empty, create a new node with a given value and set it as a root, increase the heap size to 1, and stop the insertion process.
2. calculate the next free position by adding 1 to current heap size. ("next_position = self.size+1
3. convert the position into binary and remove the leading 1 to determine the path from the root. For example, if the nexy free position is 6, its binary representation is 110, then removing the  leading 1, the remaining path is 10, meaning right first and then left.
4. start from the root and follow the path, excluding its final dogit, to locate the parent of the new node. A 0 means move to the left child, while a 1 means move to the right child.
5. create a new node containing the given value and set its parent reference to the local parent.(new_node.parent = parent)
6. connect the new node to the parent's left or right reference according to the final digit of the binary path.
7.  increase the heap size by 1 after successfully connecting the new node. ("self.size += 1")
8.  start bubbling up from the newly inserted node by comparing its value with its parent's value
9.  if the current node's value is strictly smaller than its parent's value, swap their values and move upward to the parent.
10. repeat the  comparison and swapping process until the current node's value is no longer smaller than its parent's value, or the current node reaches the root.  

step 4 Define peek()
--------------------------------------------------------------------------------








