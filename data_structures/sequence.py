"""
This is the implementation of a Sequence using the multimodal Node Object
"""

from data_types import SubDataStructure, ResponseType, DataType, NodeInterface
from data_structures.node import Node
from sys import getsizeof

class Sequence(SubDataStructure):
    """
    Variables:
        data(array): This is an array that holds all of the data
        length (int): This holds the length of the Sequence, # of Nodes
        size (int): This holds the total amount of bytes the sequence takes

    """
    def __init__(self) -> None:
       self.data = []
       self.length = 0
       self.size = 0

    """
    ********************************************************************************************************************************************
    the functions below are the ones implemented by SubDataStructure
    """
    def add(self, temp_node: NodeInterface) -> ResponseType:
        
        self.data.append(temp_node)

        self.length += 1
        self.size += getsizeof(temp_node)

        self.data = sorted(self.data, key=lambda obj: obj.key)

        return ResponseType.SUCCESS
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        #check to see if empty Sequence
        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        #check to see if index out of bounds
        if key >= self.get_length():
            return ResponseType.NODE_NOT_FOUND
        
        temp_node = self.data.pop(key)
        self.shift_keys_down(key)

        self.length -= 1
        self.size -= getsizeof(temp_node)

        return temp_node
    
    def get(self, key: int) -> NodeInterface or ResponseType:
        #check to see if empty Sequence
        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        #check to see if index out of bounds
        if key >= self.get_length():
            return ResponseType.NODE_NOT_FOUND
        
        temp_node = self.data[key]

        return temp_node

    def update(self, key: int, value: any) -> ResponseType:
        #check to see if empty Sequence
        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        #check to see if index out of bounds
        if key >= self.get_length():
            return ResponseType.NODE_NOT_FOUND
        
        self.data[key].update_value(value)

        return ResponseType.SUCCESS

    
    def get_length(self) -> int:
        return self.length
    
    def get_size(self) -> int:
        return self.size
    
    def iterate(self, iterate_function) -> ResponseType:
        for node in self.data:
            iterate_function(node)

    def print_metadata(self) -> ResponseType:
        print("Length: " + str(self.length))
        print("Size: " + str(self.size))

        return ResponseType.SUCCESS
    
    """
    ********************************************************************************************************************************************
    the functions below are the helper methods
    """

    #returns bool for is the sequence is empty
    def is_empty(self) -> bool:
        return self.length == 0
    
    #shifts keys of Nodes down when Node is removed and 
    def shift_keys_down(self, index) -> ResponseType:
        for i in range(index, self.get_length() -1):
            new_key = self.data[i].get_key() -1
            self.data[i].update_key(new_key)
        return ResponseType.SUCCESS