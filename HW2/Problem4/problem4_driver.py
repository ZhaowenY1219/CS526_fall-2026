from problem4 import SortedDoublyLinkedList


def main():
    linked_list = SortedDoublyLinkedList()

    for line_number, line in enumerate(__import__("sys").stdin, start=1):
        line = line.strip()

        # Ignore blank lines and comments
        if not line or line.startswith("#"):
            continue

        parts = line.split()
        command = parts[0].lower()
        arguments = parts[1:]

        try:
            if command == "add":
                if len(arguments) != 1:
                    print(f"line {line_number}: expected 'add <value>', got '{line}'")
                    continue

                value = float(arguments[0])

                if value.is_integer():
                    value = int(value)

                linked_list.add(value)

            elif command == "delete":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: expected 'delete <value>', got '{line}'"
                    )
                    continue

                value = float(arguments[0])

                if value.is_integer():
                    value = int(value)

                linked_list.delete(value)

            elif command == "exists":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: expected 'exists <value>', got '{line}'"
                    )
                    continue

                value = float(arguments[0])

                if value.is_integer():
                    value = int(value)

                print(linked_list.exists(value))

            elif command == "count":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: expected 'count <value>', got '{line}'"
                    )
                    continue

                value = float(arguments[0])

                if value.is_integer():
                    value = int(value)

                print(linked_list.count(value))

            elif command == "print_list":
                if len(arguments) != 0:
                    print(
                        f"line {line_number}: expected 'print_list', got '{line}'"
                    )
                    continue

                linked_list.print_list()

            elif command == "total":
                if len(arguments) != 0:
                    print(f"line {line_number}: expected 'total', got '{line}'")
                    continue

                print(linked_list.total())

            elif command == "sum_middle_three":
                if len(arguments) != 0:
                    print(
                        f"line {line_number}: expected 'sum_middle_three', got '{line}'"
                    )
                    continue

                print(linked_list.sum_middle_three())

            elif command == "median":
                if len(arguments) != 0:
                    print(f"line {line_number}: expected 'median', got '{line}'")
                    continue

                print(linked_list.median())

            else:
                print(f"line {line_number}: unknown directive '{command}'")

        except ValueError as error:
            print(f"line {line_number}: {error}")


if __name__ == "__main__":
    main()
