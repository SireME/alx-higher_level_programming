class Node:
    """Create singly linked list node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data from node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data for node"""
        if not isinstance(value, int):
            raise TypeError("Data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node"""
        if (value is not None) and (not isinstance(value, Node)):
            raise TypeError("Next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create singly linked list"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """Insert node at appropriate position to maintain sorted order"""
        new_node = Node(value)
        if self.head is None:
            # If list is empty, new node becomes the head
            self.head = new_node
        elif value < self.head.data:
            # If the value is smaller than the head, new node becomes the new head
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
