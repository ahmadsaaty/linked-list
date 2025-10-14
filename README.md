Implement your own class in Python using two classes:
1.Node:
    Attributes: value (for data), next (references the next node, also of type Node, default None)
    Methods: __init__
2. LinkedList:
    Attributes: head (the first node in the LL)
    Methods:
    def __init__(...) # The init method
    def insert_at_beginning(self, value):  # Add a new node at the start
    def insert_at_end(self, value):        # Add a new node at the end
    def delete_value(self, value):         # Remove the first node with given value
    def search(self, value):               # Return True if value exists, else False
    def display(self):                     # Print list values like: 5 -> 10 -> 12 -> None
PS: No need to insert in the middle
----------------------------------------------------------------------
Code sample
`````````````````````````````````````````````
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)
linked_list.display()   # Output: 5 -> 10 -> 20 -> None

linked_list.delete_value(10)
linked_list.display()   # Output: 5 -> 20 -> None

print(linked_list.search(20))  # Output: True
print(linked_list.search(50))  # Output: False
`````````````````````````````````````````````