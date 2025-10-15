# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0301
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self,node:Node):
        self.node= node
        self.head= None

    def insert_at_beginning(self, value):
        pass

    def insert_at_end(self, value):
        pass

    def delete_value(self, value):
        pass

    def search(self, value):
        pass

    def display(self):
        pass


linked_list= LinkedList(10)
print(linked_list.node,end="-->")
# linked_list.head = 