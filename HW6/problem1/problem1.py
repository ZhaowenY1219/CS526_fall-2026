
import ast
import sys


# ============================================================
# Step 1: Read the Input and Initialize the Data
# ============================================================

def merge_sorted_logs(logs):

    # Number of registers
    k = len(logs)

    # Track the next unprocessed sale in each register
    positions = [0] * k

    # Store the final merged (time, register) pairs
    result = []


    # ========================================================
    # Step 2: Implement a Custom Min-Priority Queue
    # ========================================================

    class MinPriorityQueue:

        def __init__(self):
            # Store priority queue entries in a binary min-heap
            self.items = []

        # Compare two entries using time first,
        # then register number when times are equal
        def _has_higher_priority(self, first, second):

            if first[0] != second[0]:
                return first[0] < second[0]

            return first[1] < second[1]

        # Insert a new entry and restore heap order
        # through bubbling up
        def insert(self, entry):

            self.items.append(entry)

            current = len(self.items) - 1

            while current > 0:

                parent = (current - 1) // 2

                if self._has_higher_priority(
                    self.items[current],
                    self.items[parent]
                ):

                    self.items[current], self.items[parent] = (
                        self.items[parent],
                        self.items[current]
                    )

                    current = parent

                else:
                    break

        # Remove and return the highest-priority entry
        # then restore heap order through bubbling down
        def remove_min(self):

            if self.is_empty():
                raise IndexError("Priority queue is empty")

            min_entry = self.items[0]

            # Remove the last entry
            last_entry = self.items.pop()

            # Move the last entry to the root if entries remain
            if self.items:

                self.items[0] = last_entry

                current = 0
                size = len(self.items)

                # Restore heap order through bubbling down
                while True:

                    left = 2 * current + 1
                    right = 2 * current + 2

                    smallest = current

                    if (
                        left < size
                        and self._has_higher_priority(
                            self.items[left],
                            self.items[smallest]
                        )
                    ):
                        smallest = left

                    if (
                        right < size
                        and self._has_higher_priority(
                            self.items[right],
                            self.items[smallest]
                        )
                    ):
                        smallest = right

                    if smallest == current:
                        break

                    self.items[current], self.items[smallest] = (
                        self.items[smallest],
                        self.items[current]
                    )

                    current = smallest

            return min_entry

        # Check whether the priority queue is empty
        def is_empty(self):

            return len(self.items) == 0

    # ========================================================
    # Step 3: Initialize the Priority Queue
    # ========================================================

    priority_queue = MinPriorityQueue()

    # Insert the first sale from each non-empty register
    for index in range(k):

        if logs[index]:

            register = index + 1

            first_sale = logs[index][0]

            priority_queue.insert((first_sale, register))

            # The first sale has been inserted into the queue.
            # This index points to the next sale.
            positions[index] = 1

    # ========================================================
    # Step 4: Merge the Sales Logs
    # ========================================================

    while not priority_queue.is_empty():

        # Remove the entry with the highest priority
        time, register = priority_queue.remove_min()

        # Add the entry to the final result
        result.append((time, register))

        # Find the corresponding register's log
        log_index = register - 1

        # Get the position of its next unprocessed sale
        next_position = positions[log_index]

        # If another sale is available, insert it into the queue
        if next_position < len(logs[log_index]):

            next_time = logs[log_index][next_position]

            priority_queue.insert((next_time, register))

            # Move the position index forward
            positions[log_index] += 1

    # ========================================================
    # Step 5: Return the Merged Result
    # ========================================================

    return result


# ============================================================
# Main Program
# ============================================================

def main():

    # Read one register's sales log per line
    input_lines = [
        line.strip()
        for line in sys.stdin
        if line.strip()
    ]

    try:

        # Convert each input line into a Python list
        logs = [
            ast.literal_eval(line)
            for line in input_lines
        ]

        # Check that every register log is a list
        if not all(isinstance(log, list) for log in logs):
            raise ValueError("Each register log must be a list")

    except (SyntaxError, ValueError) as error:

        print(f"Invalid input: {error}", file=sys.stderr)
        return

    # Merge all register logs
    result = merge_sorted_logs(logs)

    # Print the merged result
    print(result)


if __name__ == "__main__":
    main()
