
import ast
import os
import sys


# ============================================================
# Step 1: Initialize Two Heaps
# ============================================================

# Import the Heap implementation from Problem 2
problem2_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "Problem2")
)

if problem2_path not in sys.path:
    sys.path.insert(0, problem2_path)

from problem2 import Heap


# Extend the Min-Heap from Problem 2 to support a Max-Heap
class MaxHeap(Heap):

    # Restore the Max-Heap order through bubbling up
    def _bubble_up(self, current):

        while current.parent is not None and current.value > current.parent.value:

            current.value, current.parent.value = (
                current.parent.value,
                current.value
            )

            current = current.parent

    # Restore the Max-Heap order through bubbling down
    def _bubble_down(self, current):

        while current.left is not None:

            # Start with the left child
            larger_child = current.left

            # Select the larger child if the right child exists
            if (
                current.right is not None
                and current.right.value > current.left.value
            ):
                larger_child = current.right

            # Stop if the current value is already larger
            if current.value >= larger_child.value:
                break

            # Swap values and move downward
            current.value, larger_child.value = (
                larger_child.value,
                current.value
            )

            current = larger_child

    # Remove and return the maximum value at the root
    def extract_max(self):

        # Reuse the root-removal procedure from Problem 2.
        # The overridden _bubble_down() restores Max-Heap order.
        return super().extract_min()


# ============================================================
# Step 2: Read the Input and Initialize the Result List
# ============================================================

def main():

    # Read the sales amounts as a single list from standard input
    raw_input = sys.stdin.read().strip()

    if not raw_input:
        sales = []
    else:
        try:
            sales = ast.literal_eval(raw_input)

        except (SyntaxError, ValueError):
            print("Error: input must be a valid list.", file=sys.stderr)
            return

    # Check that the input is a list
    if not isinstance(sales, list):
        print("Error: input must be a list.", file=sys.stderr)
        return

    # Initialize the two heaps
    lower_heap = MaxHeap()
    upper_heap = Heap()

    # Initialize the running median result list
    running_medians = []

    # If the input list is empty, print an empty list and stop
    if not sales:
        print(running_medians)
        return


    # ========================================================
    # Step 3: Insert Each Sale into the Appropriate Heap
    # ========================================================

    for sale in sales:

        # Insert the new sale into the appropriate heap
        if lower_heap.is_empty() or sale <= lower_heap.peek():

            lower_heap.insert(sale)

        else:

            upper_heap.insert(sale)


        # ====================================================
        # Step 4: Rebalance the Two Heaps
        # ====================================================

        # Move the maximum value from lower_heap to upper_heap
        # if lower_heap contains more than one extra value
        while len(lower_heap) > len(upper_heap) + 1:

            value = lower_heap.extract_max()
            upper_heap.insert(value)

        # Move the minimum value from upper_heap to lower_heap
        # if upper_heap contains more values
        while len(upper_heap) > len(lower_heap):

            value = upper_heap.extract_min()
            lower_heap.insert(value)


        # ====================================================
        # Step 5: Calculate the Current Median
        # ====================================================

        # If both heaps have the same number of values,
        # calculate the average of their root values
        if len(lower_heap) == len(upper_heap):

            median = (
                lower_heap.peek() + upper_heap.peek()
            ) / 2.0

        # Otherwise, lower_heap contains one extra value
        else:

            median = float(lower_heap.peek())


        # ====================================================
        # Step 6: Store the Running Median
        # ====================================================

        running_medians.append(median)

    # Print all running medians after processing every sale
    print(running_medians)


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":
    main()
