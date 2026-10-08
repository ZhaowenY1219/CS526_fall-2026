from problem2 import SinglyLinkedList


def main():
    linked_list = SinglyLinkedList()
    line_number = 0

    while True:
        try:
            line = input()
        except EOFError:
            break

        line_number += 1
        line = line.strip()

        # Ignore blank lines and comments
        if line == "" or line.startswith("#"):
            continue

        parts = line.split()
        command = parts[0]
        arguments = parts[1:]

        try:
            if command == "append":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: "
                        f"expected 'append <value>', got '{line}'"
                    )
                    continue

                value = int(arguments[0])
                linked_list.append(value)

            elif command == "prepend":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: "
                        f"expected 'prepend <value>', got '{line}'"
                    )
                    continue

                value = int(arguments[0])
                linked_list.prepend(value)

            elif command == "insert":
                if len(arguments) != 2:
                    print(
                        f"line {line_number}: "
                        f"expected 'insert <index> <value>', got '{line}'"
                    )
                    continue

                try:
                    index = int(arguments[0])
                except ValueError:
                    print(
                        f"line {line_number}: "
                        f"index must be a whole number, got '{line}'"
                    )
                    continue

                value = int(arguments[1])
                linked_list.insert(index, value)

            elif command == "get":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: "
                        f"expected 'get <index>', got '{line}'"
                    )
                    continue

                try:
                    index = int(arguments[0])
                except ValueError:
                    print(
                        f"line {line_number}: "
                        f"index must be a whole number, got '{line}'"
                    )
                    continue

                value = linked_list.get(index)
                print(f"get({index}) = {value}")

            elif command == "find":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: "
                        f"expected 'find <value>', got '{line}'"
                    )
                    continue

                value = int(arguments[0])
                position = linked_list.find(value)

                print(f"find({value}) = {position}")

            elif command == "len":
                if len(arguments) != 0:
                    print(
                        f"line {line_number}: "
                        f"expected 'len', got '{line}'"
                    )
                    continue

                print(f"len = {len(linked_list)}")

            elif command == "update":
                if len(arguments) != 2:
                    print(
                        f"line {line_number}: "
                        f"expected 'update <index> <value>', got '{line}'"
                    )
                    continue

                try:
                    index = int(arguments[0])
                except ValueError:
                    print(
                        f"line {line_number}: "
                        f"index must be a whole number, got '{line}'"
                    )
                    continue

                value = int(arguments[1])
                linked_list.update(index, value)

            elif command == "delete":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: "
                        f"expected 'delete <value>', got '{line}'"
                    )
                    continue

                value = int(arguments[0])

                if linked_list.find(value) == -1:
                    print(
                        f"line {line_number}: "
                        f"{value} not found, nothing deleted"
                    )
                    continue

                linked_list.delete(value)

            elif command == "delete_at":
                if len(arguments) != 1:
                    print(
                        f"line {line_number}: "
                        f"expected 'delete_at <index>', got '{line}'"
                    )
                    continue

                try:
                    index = int(arguments[0])
                except ValueError:
                    print(
                        f"line {line_number}: "
                        f"index must be a whole number, got '{line}'"
                    )
                    continue

                value = linked_list.delete_at(index)
                print(f"delete_at({index}) = {value}")

            elif command == "print_list":
                if len(arguments) != 0:
                    print(
                        f"line {line_number}: "
                        f"expected 'print_list', got '{line}'"
                    )
                    continue

                linked_list.print_list()

            else:
                print(
                    f"line {line_number}: "
                    f"unknown directive '{command}'"
                )

        except IndexError:
            # This handles indexes that are outside the list.
            if command in ("get", "delete_at", "update", "insert"):
                index = arguments[0]
                print(
                    f"line {line_number}: "
                    f"index {index} out of range"
                )

        except ValueError:
            print(
                f"line {line_number}: "
                f"invalid value in '{line}'"
            )

    print("Final list:", end=" ")
    linked_list.print_list()


if __name__ == "__main__":
    main()
