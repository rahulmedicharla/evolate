from data_structures.data_types import DataType, ErrorType
from data_structures.node import Node

#This is the implementation of the Singly Linked List using the multipurpose Node.
class SinglyLinkedList():

    """
    Each singly linked list has these variables
    
    head (Node) : this the head pointer that will always point to the head of the linked list
    tail (Node) : this is the tail pointer that will always point to the end of the linked list.
    size (int): tells how long the singly linked list is

    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_item(self, value) -> Node:
        #edge case to check for whether it is the first item in the singly linked list;
        if(self.is_empty()):
            self.head = Node(self.size, value, DataType.SINGLY_LINKED_LIST)
            self.tail = self.head
        else:
            temp_node = Node(self.size, value, DataType.SINGLY_LINKED_LIST)
            self.tail.next = temp_node
            self.tail = self.tail.next
        
        self.size += 1

    #function to iterate through linked list and print data
    def iterate(self) -> None:
        current = self.head
        while current != None:
            current.print_data()
            current = current.next

    #returns boolean for if the list is empty
    def is_empty(self) -> bool: 
        return self.size == 0
    
    #returns size of singly linked list
    def get_size(self) -> int:
        return self.size

    #function to remove a Node from the singly linked list
    def remove(self, key) -> Node or ErrorType:
        # Handle empty list scenario
        if self.head == None:
            return ErrorType.EMPTY_LIST

        # Handle case where head node needs to be removed
        if self.head.key == key:
            temp_node = self.head
            self.head = self.head.next
            return temp_node

        current = self.head
        previous = None

        # Traverse the list to find the node with the specified value
        while current != None:
            if current.key == key:
                break
            previous = current
            current = current.next

        # Node not found in the list
        if current is None:
            return ErrorType.NODE_NOT_FOUND

        # Remove the node by updating the 'next' pointers
        previous.next = current.next

        

            
