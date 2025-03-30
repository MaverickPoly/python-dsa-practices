class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        last = self.head
        while last.next is not None:
            nodes.append(str(last.value))
            last = last.next
        return " -> ".join(nodes)

    def __contains__(self, item):
        last = self.head
        while last.next is not None:
            if last.value == item:
                return True
            last = last.next
        return False

    def insert(self, value, index):
        last = self.head
        for _ in range(index - 1):
            if last.next is None:
                raise IndexError("Index out of range")
            last = last.next

        new_node = Node(value)
        new_node.next = last.next
        last.next = new_node

    def get(self, index):
        if self.head is None:
            raise IndexError("Index out of range")
        last = self.head
        for _ in range(index):
            if last.next is None:
                raise IndexError("Index out of range")
            last = last.next
        return last.value

    def delete(self, value):
        if self.head is None:
            raise ValueError("The list is empty")
        last = self.head
        while last.next is not None:
            if last.next.value == value:
                last.next = last.next.next
                break
            last = last.next

    def pop(self, index):
        if self.head is None:
            raise IndexError("Index out of range")
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            return value
        last = self.head
        for _ in range(index - 1):
            if last.next is None:
                raise IndexError("Index out of range")
            last = last.next
        value = last.next.value
        last.next = last.next.next
        return value

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            new_node = Node(value)
            last.next = new_node

    def is_empty(self):
        return True if self.head is None else False

    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.prepend(0)
    linked_list.insert(5, 2)
    # print(linked_list.pop(3))
    print(linked_list.get(0))
    print(linked_list.get(1))
    print(linked_list.get(2))
    print(linked_list.get(3))
    print(linked_list.get(4))
    print(linked_list.get(5))
    print(linked_list)
    print(0 in linked_list)
    print(6 in linked_list)

