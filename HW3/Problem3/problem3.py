# Problem 3: Reverse three types of stacks using recursion

# Step 1: Define the node classes for linked-list stacks.


class SinglyNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Step 2: Implement a stack using an array.

class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    # Return the elements from bottom to top for display.
    def bottom_to_top_values(self):
        return self.items.copy()


# Step 3: Implement a stack using a singly linked list.


class SinglyLinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = SinglyNode(value, self.top)
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    # Collect the elements from top to bottom,
    # then reverse the display list to show bottom to top.
    def bottom_to_top_values(self):
        values = []
        current = self.top

        while current is not None:
            values.append(current.value)
            current = current.next

        values.reverse()
        return values



# Step 4: Implement a stack using a doubly linked list.

class DoublyLinkedListStack:
    def __init__(self):
        self.top = None
        self.bottom = None

    def push(self, value):
        new_node = DoublyNode(value)

        # The new node becomes the top.
        new_node.next = self.top

        if self.top is None:
            # The stack was empty, so the new node
            # is also the bottom.
            self.bottom = new_node
        else:
            self.top.prev = new_node

        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        value = self.top.value
        self.top = self.top.next

        if self.top is None:
            self.bottom = None
        else:
            self.top.prev = None

        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

    # Traverse from the bottom toward the top.
    def bottom_to_top_values(self):
        values = []
        current = self.bottom

        while current is not None:
            values.append(current.value)
            current = current.prev

        return values

# Step 5: Define the recursive helper function.
# Insert a value at the bottom of the existing stack.

def insert_at_bottom(stack, value):

    # Base case:
    # If the stack is empty, put the value into it
    if stack.is_empty():
        stack.push(value)
        return

    #remove and save the top element
    top_value = stack.pop()

    # Recursively insert the target value at the bottom
    insert_at_bottom(stack, value)

    # Restore the saved top element
    stack.push(top_value)


# Step 6: Define the recursive stack-reversal function.

def reverse_stack(stack):

    # Base case:
    # An empty stack needs no reversal.
    if stack.is_empty():
        return

    # Remove and save the current top element
    value = stack.pop()

    # Recursively reverse the remaining stack
    reverse_stack(stack)

    # Insert the saved value at the bottom
    insert_at_bottom(stack, value)



# Step 7: Print the stack from bottom to top.

def print_stack(stack):
    values = stack.bottom_to_top_values()
    print(", ".join(str(value) for value in values))


# Step 8: Create, initialize, and test all three stacks.

def main():
    stacks = [
        ("Array-based Stack", ArrayStack()),
        ("Singly Linked List Stack", SinglyLinkedListStack()),
        ("Doubly Linked List Stack", DoublyLinkedListStack())
    ]

    for name, stack in stacks:

        # Push numbers 1 through 10 in order.
        for value in range(1, 11):
            stack.push(value)

        # Print the stack before reversing.
        print(name)
        print("Before: ", end="")
        print_stack(stack)

        # Reverse the same stack object recursively.
        reverse_stack(stack)

        # Print the stack after reversing.
        print("After:  ", end="")
        print_stack(stack)
        print()


if __name__ == "__main__":
    main()
