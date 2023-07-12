"""
This is the implementation of a SinglyLinkedList using a multimodal Node
"""

from data_types import SubDataStructure, ResponseType, DataType, NodeInterface
from data_structures.node import Node
from sys import getsizeof

class SinglyLinkedList(SubDataStructure):
    """
    Variables:
        head (Node): this is the head pointer that will always point to the head of the linked list
        tail (Node): this is the tail pointer that will always point to the tail of the linked list
        length (int): this is a counter holding a count of the number of Nodes
        size(int): this is the counter for how many bytes the total length is

    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
        self.size = 0

    """
    ********************************************************************************************************************************************
    the functions below are the ones implemented by SubDataStructure
    """
    def add(self, temp_node: NodeInterface) -> ResponseType:
        
        if self.is_empty():
            self.head = temp_node
            self.tail = self.head
        else:
            self.tail.next = temp_node
            self.tail = self.tail.next
        
        self.size += getsizeof(temp_node)
        self.length += 1

        return ResponseType.SUCCESS
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        # Handle empty list scenario
        if self.head == None:
            return ResponseType.EMPTY_LIST

        # Handle case where head node needs to be removed
        if self.head.get_key() == key:
            temp_node = self.head
            self.head = self.head.next
            self.size -= getsizeof(temp_node)
            self.length -= 1

            shift_node = self.head
            self.shift_keys_down(shift_node, temp_node.get_key())

            return temp_node

        current = self.head
        previous = None

        # Traverse the list to find the node with the specified value
        while current != None:
            if current.get_key() == key:
                break
            previous = current
            current = current.next

        # Node not found in the list
        if current is None:
            return ResponseType.NODE_NOT_FOUND

        # Remove the node by updating the 'next' pointers
        self.size -= getsizeof(previous.next)
        self.length -= 1
        previous.next = current.next

        shift_node = previous.next
        self.shift_keys_down(shift_node, current.get_key())

        return current
    
    def get(self, key: int) -> NodeInterface or ResponseType:

        current = self.head

        #check for empty list
        if current == None:
            return ResponseType.EMPTY_LIST
        
        #check if head is the key they are looking for
        if current.get_key() == key:
            return current
        
        # Traverse the list to find the node with the specified key
        while current != None:
            if current.get_key() == key:
                break
            current = current.next

        # Node not found in the list
        if current is None:
            return ResponseType.NODE_NOT_FOUND
        
        return current
    
    def update(self, key: int, value: any) -> ResponseType:
        current = self.head

        #check for empty list
        if current == None:
            return ResponseType.EMPTY_LIST
        
        #check if head is the key they are looking for
        if current.get_key() == key:
            current.update_value(value)
            return ResponseType.SUCCESS
        
        # Traverse the list to find the node with the specified key
        while current != None:
            if current.get_key() == key:
                break
            current = current.next

        # Node not found in the list
        if current is None:
            return ResponseType.NODE_NOT_FOUND
        
        current.update_value(value)

        return ResponseType.SUCCESS
    
    
    def get_length(self) -> int:
        return self.length
    
    def get_size(self) -> int:
        return self.size
    
    def iterate(self, iterate_function) -> ResponseType:
        current = self.head
        while current != None:
            iterate_function(current)
            current = current.next
        
        return ResponseType.SUCCESS
    
    def print_metadata(self) -> ResponseType:
        print("Length: " + str(self.length))
        print("Size: " + str(self.size))

        return ResponseType.SUCCESS
    
    
    """
    ********************************************************************************************************************************************
    the functions below are the helper methods
    """

    #returns bool for is the singly linked list is empty
    def is_empty(self) -> bool:
        return self.length == 0
    
    #shifts the keys of the Nodes down when item is removed
    def shift_keys_down(self, current: NodeInterface, old_key: int) -> ResponseType:
        while current != None:
            if current.get_key() > old_key:
                new_key = current.get_key() -1
                current.update_key(new_key)
            current = current.next

        return ResponseType.SUCCESS