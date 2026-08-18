class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        data = self.top.data
        self.top = self.top.next
        print("Popped:", data)

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.display()

stack.pop()

print("After Pop:")
stack.display()