class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append a node at the end of the list
    def append_node(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, make the new node the head
            self.head = new_node
        else:
            # Traverse to the end and add the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Search for a node with a particular value
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True  # Node found
            current = current.next
        return False  # Node not found

    # Display the list
    def display_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
        else:
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


# Example usage:

# Create the linked list
linked_list = SinglyLinkedList()

# Append nodes
linked_list.append_node(10)
linked_list.append_node(20)
linked_list.append_node(30)

# Display the list
print("Linked List:")
linked_list.display_list()

# Search for a node
print("Searching for 20 in the list:")
if linked_list.search_node(20):
    print("Node found.")
else:
    print("Node not found.")

print("Searching for 40 in the list:")
if linked_list.search_node(40):
    print("Node found.")
else:
    print("Node not found.")
