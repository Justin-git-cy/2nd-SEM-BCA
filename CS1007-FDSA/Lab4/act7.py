class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Delete the first node with the given data
    def delete_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                elif current.prev:
                    current.prev.next = current.next
                elif current.next:
                    current.next.prev = current.prev
                else current == self.head:
                    self.head = current.next
                current = None  # Free the node
                return
            current = current.next
        print(f"Node with data {data} not found.")

    # Traverse the list forward (head to tail)
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

    # Traverse the list backward (tail to head)
    def traverse_backward(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        # Move to the tail
        while current.next:
            current = current.next
        # Traverse backward from the tail
        while current:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev
        print()

# Example usage:
dll = DoublyLinkedList()

# Insert elements at the beginning
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_beginning(30)
print("Doubly linked list after inserting 30, 20, 10 at the beginning:")
dll.traverse_forward()

# Insert elements at the end
dll.insert_at_end(40)
dll.insert_at_end(50)
print("\nDoubly linked list after inserting 40, 50 at the end:")
dll.traverse_forward()

# Delete a node by value (delete 20)
dll.delete_node(20)
print("\nDoubly linked list after deleting node with value 20:")
dll.traverse_forward()

# Traverse backward
print("\nTraversing the doubly linked list backward:")
dll.traverse_backward()

