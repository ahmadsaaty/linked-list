# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0301
# pylint: disable=C0304
# pylint: disable=C0103
# pylint: disable=C0303
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# first= Node(24)
# second= Node(7)
# third=Node(9)

# first.next =second
# second.next=third

# current = first

# while current is not None:
#     print(current.data,end="-->")
#     current=current.next


class LinkedList:
    def __init__(self):
        self.head = None
    # head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = new_node
            current.next = self.head
            self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def delete_value(self, value):
        previous = None
        current = self.head
        if self.head is None:
            return

        elif current.value == value:
            self.head = current.next
            current.next = None
            print(f"item {value} deleted")
            return current

        else:
            while current is not None:
                if current.value == value:
                    break
                previous = current
                current = current.next

            previous.next = current.next
            current.next = None
            print(f"item {value} deleted")
        # self.display()

    def search(self, value):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current.next is not None:
                if current.value == value:
                    # print(current.value == value)
                    break
                else:
                    current = current.next
                   
            return (current.value == value)

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=" --> ")
                current = current.next
            print("None")


linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)
linked_list.display()

linked_list.delete_value(10)
linked_list.display()

print(linked_list.search(20))

print(linked_list.search(50))

# linked_list.insert_at_end(15)
# linked_list.insert_at_end(47)
# linked_list.insert_at_end(94)
# linked_list.insert_at_end(51)
# linked_list.insert_at_end(3)

# # linked_list.display()

# linked_list.insert_at_beginning(25)
# # linked_list.display()
# linked_list.insert_at_beginning(64)

# linked_list.display()

# 
# linked_list.delete_value(64)
# linked_list.delete_value(3)
# linked_list.delete_value(25)
# linked_list.delete_value(94)
# linked_list.delete_value(15)
# linked_list.delete_value(47)
# linked_list.delete_value(51)
# linked_list.delete_value(51)
# linked_list.delete_value(22)


# linked_list.display()

# linked_list.search(15)
# linked_list.search(25)
# linked_list.search(15)
# linked_list.search(88)
