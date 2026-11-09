import random

# Step 1: Define the Node ADT

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Step 2: Define the BST ADT

class BST:
    def __init__(self):
        self.root = None

    # Step 3: AddNode(Value)

    def AddNode(self, value):

        # If the tree is empty, create a new node as the root
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root

        while current is not None:

            # Do not insert a duplicate value
            if value == current.value:
                return

            # Move to the left subtree
            elif value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                else:
                    current = current.left

            # Move to the right subtree
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                else:
                    current = current.right

    # Step 4: FindNode(Value)

    def FindNode(self, value):

        # Start searching from the root node
        current = self.root

        while current is not None:

            if value == current.value:
                return True

            elif value < current.value:
                current = current.left

            else:
                current = current.right

        # The target value does not exist in the tree
        return False

    # Step 5: DeleteNode(Value)

    def DeleteNode(self, value):

        # Search for the node containing the target value
        current = self.root
        parent = None

        while current is not None and current.value != value:

            # Keep track of the parent node
            parent = current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        # The target value does not exist in the tree
        if current is None:
            return False

        # Case 1: The node has no children

        if current.left is None and current.right is None:

            # If the node is the root
            if parent is None:
                self.root = None

            # If the node is the parent's left child
            elif parent.left is current:
                parent.left = None

            # If the node is the parent's right child
            else:
                parent.right = None

        # Case 2: The node has one child

        elif current.left is None or current.right is None:

            # Identify the existing child
            if current.left is not None:
                child = current.left
            else:
                child = current.right

            # If the node is the root
            if parent is None:
                self.root = child

            # If the node is the parent's left child
            elif parent.left is current:
                parent.left = child

            # If the node is the parent's right child
            else:
                parent.right = child

        # Case 3: The node has two children

        else:

            # Move to the target node's left subtree
            predecessor_parent = current
            predecessor = current.left

            # Find the largest node in the left subtree
            while predecessor.right is not None:
                predecessor_parent = predecessor
                predecessor = predecessor.right

            # Copy the predecessor's value into the target node
            current.value = predecessor.value

            # Remove the predecessor from its original position

            # If the predecessor is the target node's direct left child
            if predecessor_parent is current:
                predecessor_parent.left = predecessor.left

            # If the predecessor is deeper in the left subtree
            else:
                predecessor_parent.right = predecessor.left

        # Return True after successful deletion
        return True

    # Step 6: PrintTree()

    def PrintTree(self):

        # Check whether the tree is empty
        if self.root is None:
            print("The tree is empty.")
            return

        # Start inorder traversal from the root
        self._InorderTraversal(self.root)

        # Print a newline after the traversal is completed
        print()

    def _InorderTraversal(self, current):

        # Stop the recursion if the current node is None
        if current is None:
            return

        # Visit the left subtree
        self._InorderTraversal(current.left)

        # Print the current node
        print(current.value, end=" ")

        # Visit the right subtree
        self._InorderTraversal(current.right)



# Example usage

if __name__ == "__main__":

    tree = BST()

    # Randomly generate an input set with a size between 5 and 50
    # Each value is between 1 and 1000
    input_size = random.randint(5, 50)
    input_set = random.sample(range(1, 1001), input_size)

    # Print the input set
    print("Input set:", input_set)

    # Create the initial BST
    for value in input_set:
        tree.AddNode(value)

    # Print the initial BST
    print("\nInitial BST:")
    tree.PrintTree()

    # Test AddNode()
    # Generate a new value that does not already exist in the tree
    while True:
        add_value = random.randint(1, 1000)
        if add_value not in input_set:
            break

    print(f"\nAfter AddNode({add_value}):")
    tree.AddNode(add_value)
    tree.PrintTree()

    # Test FindNode() - Positive case
    # Randomly select a value that exists in the tree
    found_value = random.choice(input_set)

    print(f"\nFindNode({found_value}):", tree.FindNode(found_value))

    # Test FindNode() - Negative case
    # Randomly generate a value that does not exist in the tree
    existing_values = set(input_set)
    existing_values.add(add_value)

    while True:
        missing_value = random.randint(1, 1000)
        if missing_value not in existing_values:
            break

    print(f"FindNode({missing_value}):", tree.FindNode(missing_value))

    # Test DeleteNode()
    # Randomly select an existing value to delete
    delete_value = random.choice(input_set)

    print(f"\nAfter DeleteNode({delete_value}):")
    tree.DeleteNode(delete_value)
    tree.PrintTree()
