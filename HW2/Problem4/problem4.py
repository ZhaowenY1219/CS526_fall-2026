class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class SortedDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count_nodes = 0

    def __len__(self):
        return self.count_nodes

    def add(self, value):
        new_node = Node(value)

        # Case 1: empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count_nodes += 1
            return

        # Case 2: add to the head
        if value <= self.head.value:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count_nodes += 1
            return

        # Case 3: add to the tail
        if value > self.tail.value:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count_nodes += 1
            return

        # Case 4: insert in the middle
        current = self.head

        while current is not None and current.value < value:
            current = current.next

        previous = current.prev

        new_node.prev = previous
        new_node.next = current
        previous.next = new_node
        current.prev = new_node

        self.count_nodes += 1

    def delete(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                # Only one node
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None

                # Delete head
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None

                # Delete tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None

                # Delete middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.count_nodes -= 1
                return True

            # Because the list is sorted, we can stop early
            if current.value > value:
                return False

            current = current.next

        return False

    def exists(self, value):
        return self._exists(self.head, value)

    def _exists(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if node.value > value:
            return False

        return self._exists(node.next, value)

    def total(self):
        return self._total(self.head)

    def _total(self, node):
        if node is None:
            return 0

        return node.value + self._total(node.next)

    def count(self, value):
        return self._count(self.head, value)

    def _count(self, node, value):
        if node is None:
            return 0

        if node.value > value:
            return 0

        if node.value == value:
            return 1 + self._count(node.next, value)

        return self._count(node.next, value)

    def sum_middle_three(self):
        if self.count_nodes < 3:
            raise ValueError("list must have at least 3 nodes")

        mid = self.count_nodes // 2
        current = self.head

        # Odd number of nodes:
        # indices mid-1, mid, mid+1
        if self.count_nodes % 2 == 1:
            for _ in range(mid - 1):
                current = current.next

            return (
                current.value
                + current.next.value
                + current.next.next.value
            )

        # Even number of nodes:
        # indices mid-2, mid-1, mid
        else:
            for _ in range(mid - 2):
                current = current.next

            return (
                current.value
                + current.next.value
                + current.next.next.value
            )

    def median(self):
        if self.count_nodes == 0:
            raise ValueError("cannot find median of an empty list")

        mid = self.count_nodes // 2
        current = self.head

        for _ in range(mid):
            current = current.next

        # Odd number of nodes
        if self.count_nodes % 2 == 1:
            return current.value

        # Even number of nodes
        return (current.prev.value + current.value) / 2

    def print_list(self):
        if self.head is None:
            print("(empty)")
            return

        self._print_list(self.head)

    def _print_list(self, node):
        if node is None:
            print()
            return

        if node.next is None:
            print(node.value)
        else:
            print(node.value, end=" <-> ")
            self._print_list(node.next)
