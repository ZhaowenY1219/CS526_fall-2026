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
2. calculate the next free position by adding 1 to current heap size. ("next_position = self.size+1")
3. convert the position into binary and remove the leading 1 to determine the path from the root. For example, if the next free position is 6, its binary representation is 110, then removing the  leading 1, the remaining path is 10, meaning right first and then left.
4. start from the root and follow the path, excluding its final dogit, to locate the parent of the new node. A 0 means move to the left child, while a 1 means move to the right child.
5. create a new node containing the given value and set its parent reference to the located parent.(new_node.parent = parent)
6. connect the new node to the parent's left or right reference according to the final digit of the binary path.( if path ='0', then parent.left= new_node,otherwise, parent.right= new_node)
7.  increase the heap size by 1 after successfully connecting the new node. ("self.size += 1")
8.  start bubbling up from the newly inserted node by comparing its value with its parent's value
9.  if the current node's value is strictly smaller than its parent's value, swap their values and move upward to the parent.
10. repeat the  comparison and swapping process until the current node's value is no longer smaller than its parent's value, or the current node reaches the root.  

step 4 Define peek()
--------------------------------------------------------------------------------
1. check whether the heap is empty
2. if the heap is enpty, raise an IndexError
3. otherwise, return the value stored in the root without modifying the heap 

step 5 Define extract_min()
--------------------------------------------------------------------------------
1. check wheter the heap is empty, if it is empty, raise an ‘IndexError’
2. save the value stored in the root node as the minimum value to be returned
3. if the heap contains only one node, set the root to None, decrease the heap size to 0,and return the saved minimum value
4. locate the last node using the current heap size and its binary path,convert the position into binary and remove the leading 1 to determine the path from the root.(e.g,if the current heap size is 6, its binary representation is 110.after removing the leading 1, the remaining path is 10, meaning right first and then left
5. start from the root and follow the binary path, excluding its final digit, to locate the parent of the last node
6. use the final digit of the binary path to locate the last node
7. copy the last node's value into the root node,replacng the original root value
8. remove the last node from its original position by updating the corresponding reference of its parent
9. decrease the heap size by 1
10. start bubbling down from the root
11. compare the current node with its existing children and identify the child with the smaller value,if only one child exists,use that child for comparison
12. if the current node's value is greater than the smaller child's value, swap their values and move downward to that child
13. repeat the comparison and swapping process until the current node is no larger than its smaller child, or it has no children
14. return the saved minmum value

step 6 Define delete(value)
--------------------------------------------------------------------------------
1. start searching from the root node to find a node containing the target value
2. traverse the heap by checking the current node and then searching its left and right subtrees
3. if no matching node is found, return 'False' without changing the heap or its size
4. if the heap contains only one node, remove the root by setting it to 'None',decrease the heap size to 0, and return 'True'
5. locate the last node in the heap using the current heap size and its binary path
6. if the target node is the last node, remove it directly. If it is the root,set the root to None,otherwise, set the corresponding reference of its parent to None
7. otherwise, copy the last node's value into the target node,repalcing its original value
8. remove the last node from its original position by updating its parent's corresponding reference to 'None'
9. decrease the heap size by 1
10. compare the repalcement value with its parent's value
11. if the repalcement value is strictly smaller than its parent's value, restore the heap order by bubbling up
12. otherwise, restore the heap order by bubbling down, comparing the current node with its smaller child
13. return True after successfully deleting one copy of the target value

step 7 Define build(values)
--------------------------------------------------------------------------------
1. reset the heap by setting the root to None and the heap size to 0(self.root = 0; self.size = 0)
2. process the input values one at time in their original order
3. for each value, call insert(value) to add it to the heap
4. after each insertion, restore the heap order through bubbling up
5. continue until all input values have been inserted
6. return the completed heap

step 8 Define heap_sort()
--------------------------------------------------------------------------------
1. create a new heap as a copy of the original heap, preserving the node values and linked - node structure
2. initialize an empty result list to store the sorted values
3. while the copied heap is not empty, call extract_min() on the copied heap
4. append each extracted minimum value to the result list
5. continue until the copied heap becomes empty
6. return the result list in increasing order without modifying the origibal heap

step 9 Define 'is_empty()' and 'len()'
--------------------------------------------------------------------------------
9.1 is_empty()
1. check whether the heap size = 0
2. if the heap size = 0,return True
3. otherwise, return False

9.2 len()
1. return the current heap size

step 10 Define print_heap()
--------------------------------------------------------------------------------
1. check whether the heap is empty, if the root is 'None', print an appropriate message and stop
2. calculate the height of the heap and determine horizontal spacing based on the number of levels and the width of the node values
3. start the recursive drawing process from the root, using depth 0 and position 1
4. calculate the horizontal position of the current node based on its depth and logical tree position, then print its value at the calculated position.
5. if the current node has a left child, calculate its position using 'left_position = position * 2 + 1", print the symbol'/' between parent and the left child, and recursively dispaly the left subtree
6. if the current node has a right child, calculate its position using 'right_position = position * 2 + 1", print the symbol'\' between parent and the right child, and recursively dispaly the right subtree
7. continue recursively until all nodes have been displayed,then print the completed tree from top to bottom

step 11 Main Program
--------------------------------------------------------------------------------
1. read a list if values from the standard input
2. initialize an empty Min-heap
3. print the original input values
4. process each value in its original order
5. call insert(value) to insert the current value into the heap
6. after each insertion, call print_heap() to display the updated heap
7. continue until all input values have been inserted









