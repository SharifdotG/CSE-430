"""
Sharif Md. Yousuf
22101128

Sample Input 1:
x, ID, 2, 1, 5, 0x0FF
arr, ID, 10, 5, 10, 0x1D3
sum, INT, 4, 1, 15, 0x110
count, INT, 4, 1, 20, 0x120
temp, FLOAT, 8, 1, 25, 0x130
flag, BOOL, 1, 1, 30, 0x140

Sample Input 2:
a, ID, 2, 1, 1, 0x001
b, ID, 2, 1, 2, 0x002
c, ID, 2, 1, 3, 0x003
total, INT, 4, 1, 8, 0x100
numbers, ARRAY, 24, 6, 12, 0x200
result, FLOAT, 8, 1, 18, 0x300
"""

MAX = 10
INITIAL_TUPLE_COUNT = 6
SymbolTable = [None] * MAX


class SymbolInfo:
    def __init__(self, name, type_name, size, dimension, line_of_code, address):
        self.name = name
        self.type = type_name
        self.size = size
        self.dimension = dimension
        self.line_of_code = line_of_code
        self.address = address
        self.next = None


def getHashKey(name):
    total = 0
    for char in name:
        total += ord(char)
    return total % MAX


def search(name):
    index = getHashKey(name)
    current = SymbolTable[index]
    position = 0

    while current is not None:
        if current.name == name:
            return current, index, position
        current = current.next
        position += 1

    return None, index, -1


def insert(name, type_name, size, dimension, line_of_code, address):
    existing_node, index, _ = search(name)
    if existing_node is not None:
        print("Symbol already exists.")
        return False

    new_node = SymbolInfo(name, type_name, size, dimension, line_of_code, address)

    if SymbolTable[index] is None:
        SymbolTable[index] = new_node
    else:
        current = SymbolTable[index]
        while current.next is not None:
            current = current.next
        current.next = new_node

    print(f"Inserted '{name}' into bucket {index}.")
    return True


def delete(name):
    index = getHashKey(name)
    current = SymbolTable[index]
    previous = None

    while current is not None:
        if current.name == name:
            if previous is None:
                SymbolTable[index] = current.next
            else:
                previous.next = current.next

            print(f"Deleted '{name}' from bucket {index}.")
            return True

        previous = current
        current = current.next

    print("Symbol not found.")
    return False


def update(name, type_name, size, dimension, line_of_code, address):
    node, index, position = search(name)
    if node is None:
        print("Symbol not found.")
        return False

    if type_name != "":
        node.type = type_name
    if size != "":
        node.size = size
    if dimension != "":
        node.dimension = dimension
    if line_of_code != "":
        node.line_of_code = line_of_code
    if address != "":
        node.address = address

    print(f"Updated '{name}' in bucket {index}, position {position}.")
    return True


def show():
    print("\nCurrent Symbol Table")
    for index in range(MAX):
        print(f"Bucket {index}:", end=" ")
        current = SymbolTable[index]

        if current is None:
            print("NULL")
            continue

        while current is not None:
            print(
                f"({current.name}, {current.type}, {current.size}, "
                f"{current.dimension}, {current.line_of_code}, {current.address})",
                end=" -> ",
            )
            current = current.next
        print("NULL")


def parse_tuple_line(line):
    parts = [part.strip() for part in line.split(",")]
    if len(parts) != 6:
        return None
    return parts


def read_tuple_from_user(message):
    print(message)
    line = input("Enter: NAME, TYPE, SIZE, DIMENSION, LINE, ADDRESS\n> ").strip()
    parts = parse_tuple_line(line)

    if parts is None:
        print("Invalid input. Please enter exactly 6 comma-separated values.")
        return None

    return parts


def load_initial_tuples():
    print(f"Enter {INITIAL_TUPLE_COUNT} tuples to build the initial symbol table.")
    inserted = 0
    while inserted < INITIAL_TUPLE_COUNT:
        parts = read_tuple_from_user(f"Tuple {inserted + 1}:")
        if parts is None:
            continue
        if insert(*parts):
            inserted += 1


def handle_search():
    name = input("Enter symbol name to search: ").strip()
    node, index, position = search(name)

    if node is None:
        print("Symbol not found.")
    else:
        print(f"Found in bucket {index}, position {position}.")
        print(
            f"Name: {node.name}, Type: {node.type}, Size: {node.size}, "
            f"Dimension: {node.dimension}, Line: {node.line_of_code}, Address: {node.address}"
        )


def handle_insert():
    parts = read_tuple_from_user("Insert a new symbol:")
    if parts is not None:
        insert(*parts)


def handle_update():
    name = input("Enter symbol name to update: ").strip()
    print("Enter new values. Leave blank to keep old value.")
    type_name = input("New TYPE: ").strip()
    size = input("New SIZE: ").strip()
    dimension = input("New DIMENSION: ").strip()
    line_of_code = input("New LINE OF CODE: ").strip()
    address = input("New ADDRESS: ").strip()
    update(name, type_name, size, dimension, line_of_code, address)


def handle_delete():
    name = input("Enter symbol name to delete: ").strip()
    delete(name)


def print_menu():
    print("\nChoose an operation:")
    print("1. Show Symbol Table")
    print("2. Search Symbol")
    print("3. Insert Symbol")
    print("4. Update Symbol")
    print("5. Delete Symbol")
    print("6. Exit")


def main():
    load_initial_tuples()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show()
        elif choice == "2":
            handle_search()
        elif choice == "3":
            handle_insert()
        elif choice == "4":
            handle_update()
        elif choice == "5":
            handle_delete()
        elif choice == "6":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
