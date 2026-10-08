class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.count += 1

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def insert(self, index, value):
        if index < 0 or index > self.count:
            raise IndexError(f"index {index} out of range")

        if index == 0:
            self.prepend(value)
            return

        if index == self.count:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.count += 1

    def get(self, index):
        if index < 0 or index >= self.count:
            raise IndexError(f"index {index} out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.value

    def find(self, value):
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index

            current = current.next
            index += 1

        return -1

    def update(self, index, value):
        if index < 0 or index >= self.count:
            raise IndexError(f"index {index} out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        current.value = value

    def delete(self, value):
        if self.head is None:
            return

        # Delete the head node
        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

            self.count -= 1
            return

        current = self.head

        while current.next is not None:

            if current.next.value == value:

                # Delete the tail
                if current.next == self.tail:
                    self.tail = current
                    current.next = None

                # Delete a middle node
                else:
                    current.next = current.next.next

                self.count -= 1
                return

            current = current.next

    def delete_at(self, index):
        if index < 0 or index >= self.count:
            raise IndexError(f"index {index} out of range")

        # Delete the head
        if index == 0:
            value = self.head.value

            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

            self.count -= 1
            return value

        current = self.head

        for _ in range(index - 1):
            current = current.next

        target = current.next
        value = target.value

        # Delete the tail
        if target == self.tail:
            self.tail = current
            current.next = None

        # Delete a middle node
        else:
            current.next = target.next

        self.count -= 1
        return value

    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        current = self.head
        values = []

        while current is not None:
            values.append(str(current.value))
            current = current.next

        print(" -> ".join(values))
