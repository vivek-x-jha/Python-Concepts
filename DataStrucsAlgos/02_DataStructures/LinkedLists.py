# Demonstrates implementation of a linked list and helper Node class


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def __repr__(self):
        values = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            values.append(cur_node.value)
        return str(values)

    def __len__(self):
        return self.length


ll = Linkedlist()
ll.append(-3)
ll.append(1)
print(len(ll))
print(ll)
