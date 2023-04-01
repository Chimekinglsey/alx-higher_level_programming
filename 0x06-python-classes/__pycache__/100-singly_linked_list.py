#!/usr/bin/python3
"""First creating a Node class"""


class Node:
    """Call __init__() to initialize it"""
    def __init__(self, data, next_node=None):
        """Our code behaviour for class intances follow"""
        self.__data = data
        self.__next_node= next_node

    @property
    def data(self):
        """This method gets the data value passed to setter"""
        return self.__data

    @data.setter
    def data(self, value):
        """This method sets size values"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This method gets the nextnode"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This method sets next_node address"""
        if (type(value) is not None) or type(value) is not Node:
            raise TypeError("next_node must be a Node object") 
            self.__next_node = value

class SinglyLinkedList:
    """This class defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """This method will sort values in ascending order"""
        new = Node(value)
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
