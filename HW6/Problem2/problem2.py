import ast
import sys


# ============================================================
# Step 1: Define the Node ADT
# ============================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# ============================================================
# Step 2: Define the Heap ADT
# ============================================================

class Heap:

    def __init__(self):
        self.root = None
        self.size = 0

    # --------------------------------------------------------
    # Helper Method: Find a node at a given position
    # Uses the binary path to locate the node.
    # --------------------------------------------------------

    def _get_node_at_position(self, position):

        if self.root is None or position < 1 or position > self.size:
            return None

        current = self.root

        # Remove the leading 1 from the binary position
        path = bin(position)[3:]

        # Follow the path from the root
        for direction in path:

            if direction == '0':
                current = current.left
            else:
                current = current.right

            if current is None:
                return None

        return current

    # --------------------------------------------------------
    # Helper Method: Bubbling Up
    # --------------------------------------------------------

    def _bubble_up(self, current):

        while current.parent is not None and current.value < current.parent.value:

            # Swap the values of the current node and its parent
            current.value, current.parent.value = (
                current.parent.value,
                current.value
            )

            # Move upward to the parent
            current = current.parent

    # --------------------------------------------------------
    # Helper Method: Bubbling Down
    # --------------------------------------------------------

    def _bubble_down(self, current):

        while current.left is not None:

            # Start by selecting the left child
            smaller_child = current.left

            # Compare with the right child if it exists
            if current.right is not None and current.right.value < current.left.value:
                smaller_child = current.right

            # Stop if the current node is no larger than its smaller child
            if current.value <= smaller_child.value:
                break

            # Swap values
            current.value, smaller_child.value = (
                smaller_child.value,
                current.value
            )

            # Move downward to the smaller child
            current = smaller_child

    # ========================================================
    # Step 3: Define insert(value)
    # ========================================================

    def insert(self, value):

        new_node = Node(value)

        # Case 1: The heap is empty
        if self.root is None:

            self.root = new_node
            self.size = 1
            return

        # Find the next free position
        next_position = self.size + 1

        # Convert the position into a binary path
        path = bin(next_position)[3:]

        # Locate the parent of the new node
        parent = self.root

        for direction in path[:-1]:

            if direction == '0':
                parent = parent.left
            else:
                parent = parent.right

        # Connect the new node to its parent
        new_node.parent = parent

        # Connect the new node to the correct child reference
        if path[-1] == '0':
            parent.left = new_node
        else:
            parent.right = new_node

        # Increase the heap size
        self.size += 1

        # Restore the heap order through bubbling up
        self._bubble_up(new_node)

    # ========================================================
    # Step 4: Define peek()
    # ========================================================

    def peek(self):

        # Check whether the heap is empty
        if self.root is None:
            raise IndexError("peek from an empty heap")

        # Return the root value without removing it
        return self.root.value

    # ========================================================
    # Step 5: Define extract_min()
    # ========================================================

    def extract_min(self):

        # Check whether the heap is empty
        if self.root is None:
            raise IndexError("extract_min from an empty heap")

        # Save the minimum value
        min_value = self.root.value

        # Case 1: Only one node exists
        if self.size == 1:

            self.root = None
            self.size = 0

            return min_value

        # Locate the last node
        last_node = self._get_node_at_position(self.size)

        # Get its parent
        parent = last_node.parent

        # Move the last node's value to the root
        self.root.value = last_node.value

        # Remove the last node from its original position
        if parent.left is last_node:
            parent.left = None
        else:
            parent.right = None

        # Clear the removed node's parent reference
        last_node.parent = None

        # Decrease the heap size
        self.size -= 1

        # Restore the heap order through bubbling down
        self._bubble_down(self.root)

        # Return the saved minimum value
        return min_value

    # ========================================================
    # Step 6: Define delete(value)
    # ========================================================

    # Helper Method: Search for a node using tree traversal

    def _find_node(self, current, value):

        # Stop if the current node does not exist
        if current is None:
            return None

        # Check the current node
        if current.value == value:
            return current

        # Search the left subtree
        found = self._find_node(current.left, value)

        if found is not None:
            return found

        # Search the right subtree
        return self._find_node(current.right, value)

    def delete(self, value):

        # Find the target node
        target = self._find_node(self.root, value)

        # Return False if the target does not exist
        if target is None:
            return False

        # Case 1: Only one node exists
        if self.size == 1:

            self.root = None
            self.size = 0

            return True

        # Locate the last node
        last_node = self._get_node_at_position(self.size)

        # Case 2: The target node is already the last node
        if target is last_node:

            parent = last_node.parent

            if parent.left is last_node:
                parent.left = None
            else:
                parent.right = None

            last_node.parent = None

            self.size -= 1

            return True

        # Case 3: Replace the target node's value
        target.value = last_node.value

        # Remove the last node from its original position
        parent = last_node.parent

        if parent.left is last_node:
            parent.left = None
        else:
            parent.right = None

        last_node.parent = None

        # Decrease the heap size
        self.size -= 1

        # Decide which direction is needed to restore heap order
        if target.parent is not None and target.value < target.parent.value:

            # The replacement value is smaller than its parent
            self._bubble_up(target)

        else:

            # Restore the heap order by bubbling down
            self._bubble_down(target)

        return True

    # ========================================================
    # Step 7: Define build(values)
    # ========================================================

    def build(self, values):

        # Reset the heap
        self.root = None
        self.size = 0

        # Insert values one at a time in their original order
        for value in values:
            self.insert(value)

        return self

    # ========================================================
    # Step 8: Define heap_sort()
    # ========================================================

    # Helper Method: Create an independent copy of the heap

    def _copy_subtree(self, node, parent=None):

        if node is None:
            return None

        # Create a new node with the same value
        copied_node = Node(node.value)

        # Connect the copied node to its new parent
        copied_node.parent = parent

        # Recursively copy the left and right subtrees
        copied_node.left = self._copy_subtree(
            node.left, copied_node
        )

        copied_node.right = self._copy_subtree(
            node.right, copied_node
        )

        return copied_node

    def heap_sort(self):

        # Create a new, independent heap
        copied_heap = Heap()

        copied_heap.root = self._copy_subtree(self.root)
        copied_heap.size = self.size

        # Store sorted values in a result list
        result = []

        # Repeatedly extract the minimum from the copied heap
        while not copied_heap.is_empty():

            result.append(copied_heap.extract_min())

        # Return the sorted result without changing the original heap
        return result

    # ========================================================
    # Step 9: Define is_empty() and __len__()
    # ========================================================

    def is_empty(self):

        return self.size == 0

    def __len__(self):

        return self.size

    # ========================================================
    # Step 10: Define print_heap()
    # ========================================================

    # Helper Method: Calculate the height of the heap

    def _get_height(self, node):

        if node is None:
            return 0

        return 1 + max(
            self._get_height(node.left),
            self._get_height(node.right)
        )

    # Helper Method: Find the maximum width of node values

    def _get_max_label_width(self, node):

        if node is None:
            return 0

        current_width = len(str(node.value))

        return max(
            current_width,
            self._get_max_label_width(node.left),
            self._get_max_label_width(node.right)
        )

    def print_heap(self):

        # Check whether the heap is empty
        if self.root is None:
            print("The heap is empty.")
            return

        # Calculate the heap height and node label width
        height = self._get_height(self.root)
        max_label_width = self._get_max_label_width(self.root)

        # Determine the horizontal spacing
        slot_width = max_label_width + 4
        total_width = (2 ** (height - 1)) * slot_width
        row_count = 2 * height - 1

        # Temporary character grid for drawing the tree.
        # The heap nodes themselves remain stored as linked nodes.
        rows = [
            [' '] * total_width
            for _ in range(row_count)
        ]

        # Calculate the horizontal center of a node
        def get_center(depth, position):

            level_index = position - (2 ** depth)
            slots = 2 ** (height - depth - 1)

            return (
                (2 * level_index + 1) * slots * slot_width
            ) // 2

        # Recursively draw nodes and connecting symbols
        def draw(current, depth, position):

            if current is None:
                return

            center = get_center(depth, position)

            # Print the current node's value
            label = str(current.value)
            start = center - len(label) // 2

            for offset, character in enumerate(label):

                column = start + offset

                if 0 <= column < total_width:
                    rows[2 * depth][column] = character

            # Draw the left child and its connection
            if current.left is not None:

                left_position = position * 2

                left_center = get_center(
                    depth + 1,
                    left_position
                )

                connector_column = (center + left_center) // 2

                rows[2 * depth + 1][connector_column] = '/'

                draw(
                    current.left,
                    depth + 1,
                    left_position
                )

            # Draw the right child and its connection
            if current.right is not None:

                right_position = position * 2 + 1

                right_center = get_center(
                    depth + 1,
                    right_position
                )

                connector_column = (center + right_center) // 2

                rows[2 * depth + 1][connector_column] = '\\'

                draw(
                    current.right,
                    depth + 1,
                    right_position
                )

        # Start drawing from the root
        draw(self.root, 0, 1)

        # Print the completed tree from top to bottom
        for row in rows:
            print(''.join(row).rstrip())


# ============================================================
# Step 11: Main Program
# ============================================================

def main():

    # Read the input list from standard input
    raw_input = sys.stdin.read().strip()

    if not raw_input:
        values = []

    else:
        try:
            values = ast.literal_eval(raw_input)

        except (SyntaxError, ValueError):
            print(
                "Error: input must be a Python list, "
                "such as [8, 3, 5, 1].",
                file=sys.stderr
            )
            return

    if not isinstance(values, list):
        print("Error: input must be a list of values.", file=sys.stderr)
        return

    # Initialize an empty Min-Heap
    heap = Heap()

    # Print the original input values
    print("Input values:", values)

    # Insert values one at a time in their original order
    for value in values:

        heap.insert(value)

        # Print the heap after each insertion
        print(f"\nAfter insert({value}):")
        heap.print_heap()


if __name__ == "__main__":
    main()
