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


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print("Dequeued:", data)

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# --- Stack Execution ---
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.display()

stack.pop()

print("After Pop:")
stack.display()

# --- Queue Execution ---
queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)

print("\nQueue:")
queue.display()

queue.dequeue()

print("After Dequeue:")
queue.display()
