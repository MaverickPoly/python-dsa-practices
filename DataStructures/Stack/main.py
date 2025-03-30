class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # O(n)
    def __contains__(self, item):
        last = self.top
        while self.top.next is not None:
            if last.value == item:
                return True
            last = last.next
        return False

    # O(1)
    def __len__(self):
        return self.count

    # O(1)
    def pop(self):
        current_val = self.peek()
        last = self.top.next
        self.top.next = None
        self.top = last
        self.count -= 1
        return current_val

    # O(1)
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value

    # O(1)
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    # O(1)
    def is_empty(self):
        return self.count == 0

    # O(1)
    def clear(self):
        self.count = 0
        self.top = None

    def __repr__(self):
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return ", ".join(items)



if __name__ == "__main__":
    stack = Stack()
    print(stack)
    print(stack.is_empty())
    print(len(stack))

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack)
    print(stack.is_empty())


