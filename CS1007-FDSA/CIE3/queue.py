class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def front_data(self):
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def dequeue(self):
        if self.front is None:
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed_data

    def get_size(self):
        return self.size

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.front_data())
print("Dequeue:", q.dequeue())
print("Is empty:", q.is_empty())
print("Size of queue:", q.get_size())

q.dequeue()
q.dequeue()

print("Is empty:", q.is_empty())
print("Front element :", q.front_data())


