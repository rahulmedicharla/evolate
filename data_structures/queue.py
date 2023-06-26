"""
This is the implementation of a Queue using the multimodal Node Object
"""

from data_types import SubDataStructure, ResponseType, DataType, NodeInterface
from data_structures.node import Node
from sys import getsizeof

class Queue(SubDataStructure):
    """
    Variables:
        data(array): This is an array that holds all of the data
        length (int): This holds the length of the queue, # of Nodes
        size (int): This holds the total amount of bytes the Queue takes

    """
    def __init__(self) -> None:
       self.data = []
       self.length = 0
       self.size = 0

    """
    ********************************************************************************************************************************************
    the functions below are the ones implemented by SubDataStructure
    """
    def add(self, value: any) -> ResponseType:
        self.enqueue(value)

        return ResponseType.SUCCESS
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        #check to see if empty Queue
        if self.get_length() == 0:
            return ResponseType.EMPTY_LIST
        
        #check if the front of the queue is what should be gotten
        if self.front().get_key() == key:
            temp_node = self.dequeue()
            return temp_node
        
        #rotate queue to find specified key or return back to 0 index
        self.rotate()
        while self.front().get_key() != key and self.front().get_key() != 0:
            self.rotate()

        #Looped back to beginning
        if self.front().get_key() == 0:
            return ResponseType.NODE_NOT_FOUND
        
        temp_node = self.dequeue()

        return temp_node

    
    def get(self, key: int) -> NodeInterface or ResponseType:
        #check to see if empty Queue
        if self.get_length() == 0:
            return ResponseType.EMPTY_LIST
        
        #check if the front of the queue is what should be gotten
        if self.front().get_key() == key:
            temp_node = self.front()
            return temp_node
        
        #rotate queue to find specified key or return back to 0 index
        self.rotate()
        while self.front().get_key() != key and self.front().get_key() != 0:
            self.rotate()

        #Looped back to beginning
        if self.front().get_key() == 0:
            return ResponseType.NODE_NOT_FOUND
        
        temp_node = self.front()

        while(self.front().get_key() != 0):
            self.rotate()

        return temp_node


    def update(self, key: int, value: any) -> ResponseType:
        #check to see if empty Queue
        if self.get_length() == 0:
            return ResponseType.EMPTY_LIST
        
        #check if the front of the queue is what should be gotten
        if self.front().get_key() == key:
            self.front().update_value(value)
            return ResponseType.SUCCESS
        
        #rotate queue to find specified key or return back to 0 index
        self.rotate()
        while self.front().get_key() != key and self.front().get_key() != 0:
            self.rotate()

        #Looped back to beginning
        if self.front().get_key() == 0:
            return ResponseType.NODE_NOT_FOUND
        
        self.front().update_value(value)

        while(self.front().get_key() != 0):
            self.rotate()

        return ResponseType.SUCCESS

    
    def get_length(self) -> int:
        return self.length
    
    def get_size(self) -> int:
        return self.size
    
    def iterate(self, iterate_function) -> ResponseType:
        #add checks for empty list
        if self.get_length() == 0:
            return ResponseType.EMPTY_LIST
        
        iterate_function(self.front())

        #add check for list with one unit
        if self.get_length() != 1:
            self.rotate()
            while self.front().get_key() != 0:
                iterate_function(self.front())
                self.rotate()


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
    
    #shifts keys of Nodes down when Node is removed and rotate back to beginning
    def shift_keys_down(self) -> ResponseType:
       while(self.front().get_key() != 0):
           self.front().update_key(self.front().get_key() -1)
           self.rotate()
    
    #This function enqueues a Node to the end of the list
    def enqueue(self, value: any) -> None:
        temp_node = Node(self.length, value, DataType.QUEUE)
        self.data.append(temp_node)
        self.length += 1
        self.size += getsizeof(temp_node)
       
    #This function deqeueues a Node from the beginning of the list
    def dequeue(self) -> NodeInterface:
       temp_node = self.data.pop(0)
       self.length -= 1
       self.size -= getsizeof(temp_node)

       if self.length > 0:
        self.shift_keys_down()

       return temp_node
    
    #This function rotates the data array by one unit 
    def rotate(self) -> None:
        temp_node = self.data.pop(0)
        self.data.append(temp_node)
        
    #this function just exposes the front of the queue
    def front(self) -> NodeInterface:
        return self.data[0]