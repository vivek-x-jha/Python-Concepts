class _Node:
    def __init__(self, value=None):
        __slots__ = ('_value', '_next')

        self._value = value
        self._next = None


class Linkedlist:
    """A linear container data structure that provides O(1) time insertion/deletion of items
    to/from the head and tail of the sequence of values.

    Utilizes _Node object as underlying data structure
    ----------------------------------------------------
    Structure of class is as follows:

    Index 0: 1st Node <- Head Node
    Index 1: 2nd Node
    Index 2: 3rd Node
    ...
    Index n - 1: Nth Node <- Tail Node
    ----------------------------------------------------
    Methods:
    1). __getitem__(self, index)

        Time Complexity: O(n)
        Space Complexity: O(1)

    2). __delitem__(self, index)

        Time Complexity: O(n)
        Space Complexity: O(1)

    3). __iter__(self)

        Time Complexity: O(n^2)
        Space Complexity: O(1)

    4). __repr__(self)

        Time Complexity: O(n)
        Space Complexity: O(n)

    5). __str__(self)

        Time Complexity: O(n)
        Space Complexity: O(n)

    6). append(self, value)

        Time Complexity: O(1)
        Space Complexity: O(1)

    7). prepend(self, value)

        Time Complexity: O(1)
        Space Complexity: O(1)

    8). insert(self, value, index)

        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    def __init__(self, *args):
        self.head = _Node()
        self.tail = self.head
        self.size = 0
        self._iter_counter = 1
        for val in args:
            self.append(val)

    def __len__(self):
        """Returns number of non-empty nodes in Linked List"""
        return self.size

    def _get_prev_node(self, index):
        """helper method to obtain Node previous to given index in O(n) time
        i.e. if index is 1, will return 1st Node
        i.e. if size of linked list is 6 & index is -3, will return 4th Node
        """
        if index < 0:
            index += self.size
        cur_node = self.head
        prev_node_number = 1
        while prev_node_number < index:
            cur_node = cur_node._next
            prev_node_number += 1
        return cur_node

    def _is_head(self, index):
        """Helper method to determine if given index is head node"""
        if index >= self.size or index < -self.size:
            raise IndexError
        return index == 0 or index == -self.size

    def _is_tail(self, index):
        """Helper method to determine if given index is tail node"""
        if index >= self.size or index < -self.size:
            raise IndexError
        return index == -1 or index == self.size - 1

    def _get_values(self):
        """Helper method to generate string values of all node values"""
        cur_node = self.head
        for _ in range(self.size):
            yield str(cur_node._value)
            cur_node = cur_node._next

    def __getitem__(self, index):
        """Getter method to obtain value of a node at given index in O(1) time - this is considering that finding the node is encapsulated by helper method self._get_prev_node(index)
        """
        if self._is_head(index):
            return self.head._value
        else:
            prev_node = self._get_prev_node(index)
            cur_node = prev_node._next
            return cur_node._value

    def __delitem__(self, index):
        """Method to delete value of a node at given index in O(1) time - this is considering that finding the node is encapsulated by helper method self._get_prev_node(index)
        """
        if self._is_head(index):
            self.head = self.head._next
        else:
            prev_node = self._get_prev_node(index)
            prev_node._next = prev_node._next._next
            if self._is_tail(index):
                self.tail = prev_node
        self.size -= 1

    def __iter__(self):
        """Returns iterator object which user can iterate through"""
        return self

    def __next__(self):
        """Loops through iterator returning each Node value"""
        # TODO See if there's a way to improve iteration speed from quadratic to linear
        cur_node = self.head
        if self._iter_counter > self.size:
            self._iter_counter = 1
            raise StopIteration
        prev_node = self._get_prev_node(self._iter_counter)
        self._iter_counter += 1
        return prev_node._value

    def __repr__(self):
        """Provides valid Python expression that can be used to recreate an object with the same value"""
        values = ', '.join(self._get_values())
        cls_name = type(self).__name__
        return f'{cls_name}({values})'

    def __str__(self):
        """Displays printable representation of Linked List"""
        return ' -> '.join(self._get_values())

    def append(self, value):
        """Inserts node with given value to end of Linked List in O(1) time"""
        if self.head._value is None:
            self.head._value = value
        else:
            new_node = _Node(value)
            self.tail._next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value):
        """Inserts node with given value to front of Linked List in O(1) time"""
        if self.head._value is None:
            self.head._value = value
        else:
            new_node = _Node(value)
            new_node._next = self.head
            self.head = new_node
        self.size += 1

    def insert(self, value, index):
        """Inserts node with given value at a given index of Linked List in O(n) time.
        If insertion occurs at head or tail of Linked List, operation becomes O(1).
        n := len(self)
        * Index must be in interval [-n, n]
        """
        if abs(index) > self.size:
            raise IndexError
        elif self._is_head(index):
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            prev_node = self._get_prev_node(index)
            new_node = _Node(value)
            new_node._next = prev_node._next
            prev_node._next = new_node
            self.size += 1


def main():
    def disp_attributes(lnk_list_obj):
        print(f'Linked List: {lnk_list_obj}')
        print(f'\tSize: {len(lnk_list_obj)}')
        print(f'\tHead node value: {lnk_list_obj.head._value}')
        print(f'\tTail node value: {lnk_list_obj.tail._value}')

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

    print('<< Delete 1st Node >>')
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
