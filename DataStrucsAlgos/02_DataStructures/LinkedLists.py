# Demonstrates implementation of a linked list and helper Node class


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self, *args):
        self.head = Node()
        self.tail = self.head
        self.size = 0
        # Nodes indexes defined from 0, 1, ..., N - 1 (where N = self.size) but are counted as First Node, Second Node, ..., Nth-Node respectively
        self._args = args
        if len(self._args) > 0:
            for val in self._args:
                self.append(val)

    def __len__(self):
        return self.size

    def _get_prev_node(self, index):
        """gets Node previous to given index
        i.e. if index is 1, will return Node 0 (1st Node)
        i.e. if size of linked list is 6 & index is -3, will return Node 3 (4th Node)
        """
        if index < 0:
            index += self.size
        cur_node = self.head
        prev_node_number = 1
        while prev_node_number < index:
            cur_node = cur_node.next
            prev_node_number += 1
        return cur_node

    def __getitem__(self, index):
        if index >= self.size or index < -self.size:
            raise IndexError
        elif index == 0 or index == -self.size:
            return self.head.value
        else:
            prev_node = self._get_prev_node(index)
            cur_node = prev_node.next
            return cur_node.value

    def __delitem__(self, index):
        if index >= self.size or index < -self.size:
            raise IndexError
        elif index == 0 or index == -self.size:
            self.head = self.head.next
        else:
            prev_node = self._get_prev_node(index)
            prev_node.next = prev_node.next.next
            if index == -1 or index == self.size - 1:
                self.tail = prev_node
        self.size -= 1

    def __repr__(self):
        values = []
        cur_node = self.head
        for _ in range(self.size):
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
        self.size += 1

    def prepend(self, value):
        if self.head.value is None:
            self.head.value = value
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert(self, value, index):
        # Inserts node with value before given index
        if abs(index) > self.size:
            raise IndexError
        elif index == 0 or index == -self.size:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            prev_node = self._get_prev_node(index)
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1


def main():
    def disp_attributes(lnk_list_obj):
        print(f'Linked List: {lnk_list_obj}')
        print(f'\tSize: {len(lnk_list_obj)}')
        print(f'\tHead node value: {lnk_list_obj.head.value}')
        print(f'\tTail node value: {lnk_list_obj.tail.value}')

    print('<< Instantiate empty Linked List >>')
    lnk = Linkedlist()
    disp_attributes(lnk)

    print('<< Append -3, 1, 0 to Linked List >>')
    values = -3, 1, 0
    for val in values:
        lnk.append(val)
        disp_attributes(lnk)

    print('<< Prepend -12 to Linked List >>')
    lnk.prepend(-12)
    disp_attributes(lnk)

    print(f'Linked List value at first Node: {lnk[0]}')

    print('<< Instantiate Linked List with values 1, -2, -6, 0, 2 >>')
    lnk2 = Linkedlist(1, -2, -6, 0, 2)
    disp_attributes(lnk2)

    print('<< Prepend 6 to Linked List >>')
    lnk2.prepend(6)
    disp_attributes(lnk2)

    print(f'Linked List value at second Node: {lnk2[1]}')

    print('<< Delete First Node >>')
    del lnk2[0]
    disp_attributes(lnk2)

    print('<< Delete Last Node >>')
    del lnk2[-1]
    disp_attributes(lnk2)

    print('<< Append 7 to LinkedList >>')
    lnk2.append(7)
    disp_attributes(lnk2)

    print('<< Delete 3rd Node >>')
    del lnk2[2]
    disp_attributes(lnk2)

    print('<< Insert -10 before 2nd Node >>')
    lnk2.insert(-10, 1)
    disp_attributes(lnk2)


if __name__ == '__main__':
    main()
