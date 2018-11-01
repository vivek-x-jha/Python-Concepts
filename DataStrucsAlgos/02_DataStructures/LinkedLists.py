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

    def __getitem__(self, index):
        try:
            cur_node = self.head
            for _ in range(index + 1):
                cur_node = cur_node.next
            return cur_node.value
        except (KeyError, AttributeError):
            print('Index out of range')

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
print(ll.head.value, ll.tail.value)
ll.append(-3)
print(ll.head.value, ll.tail.value)
ll.append(1)
print(ll.head.value, ll.tail.value)
ll.append(0)
print(ll.head.value, ll.tail.value)
print(ll[2])
print(len(ll))
print(ll)
