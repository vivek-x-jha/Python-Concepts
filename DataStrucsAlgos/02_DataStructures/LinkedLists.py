# Demonstrates implementation of a linked list and helper Node class


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, *args):
        self.head = Node()
        self.tail = self.head
        self.length = 0
        self._args = args
        if len(self._args) > 0:
            for val in self._args:
                self.append(val)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        # TODO: When index is negative and larger than length returns head node value
        try:
            cur_node = self.head
            for _ in range(index):
                cur_node = cur_node.next
            return cur_node.value
        except AttributeError:
            return f'Error: Index {index} out of range'

    def __repr__(self):
        values = []
        cur_node = self.head
        for _ in range(len(self)):
            values.append(cur_node.value)
            cur_node = cur_node.next
        return str(values)

    def append(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length += 1


def main():
    lnk = Linkedlist()
    print(lnk.head.value, lnk.tail.value)
    lnk.append(-3)
    print(lnk.head.value, lnk.tail.value)
    lnk.append(1)
    print(lnk.head.value, lnk.tail.value)
    lnk.append(0)
    print(lnk.head.value, lnk.tail.value)
    lnk.prepend(6)
    print(lnk.head.value, lnk.tail.value)
    print(lnk[-4])
    print(len(lnk))
    print(lnk)

    lnk2 = Linkedlist(1, -2, -6, 0, 2)
    print(lnk2)
    print(len(lnk2))
    print(lnk2.head.value, lnk2.tail.value)
    lnk2.prepend(6)
    print(lnk2.head.value, lnk2.tail.value)
    print(lnk2)
    print(len(lnk2))
    print(lnk2[2])


if __name__ == '__main__':
    main()
