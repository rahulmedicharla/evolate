from data_structures.data_types import DataType, ErrorType
from data_structures.node import Node

#This is the implementation of the Sequence using the multipurpose Node.
class Sequence():

    """
    Each Sequence has these variables

    data (array): This is an array that holds all the data
    size (int) : This holds the size of the sequence
    bytes_total_size (int): This holds the total size of sequence in bytes

    """
    def __init__(self) -> None:
        self.data = []
        self.size = 0
        self.bytes_total_size = 0
    
    #function to append item to sequence
    def append(self, value) -> None:
        temp_node = Node(self.size, value, DataType.SEQUENCE)
        self.data.append(temp_node)
        self.size+= 1
        self.bytes_total_size += temp_node.size
    
    #function to remove item from sequence given a specified index of sequence
    def remove(self, index) -> Node or ErrorType:
        if self.is_empty() == True:
            return ErrorType.EMPTY_LIST
        
        if index >= self.get_size():
            return ErrorType.INDEX_OUT_OF_BOUNDS
        
        temp_node = self.data.pop(index)
        self.size -= 1
        self.bytes_total_size -= temp_node.size

        return temp_node
    
    #function to get the Node object at specified index
    def get(self, index) -> Node or ErrorType:
        if self.is_empty() == True:
            return ErrorType.EMPTY_LIST
        
        if index >= self.get_size():
            return ErrorType.INDEX_OUT_OF_BOUNDS
        
        temp_node = self.data[index]

        return temp_node

    #function to iterate through sequence and print data
    def iterate(self) -> None:
        for node in self.data:
            node.print_data()

    #returns boolean for if the sequence is empty
    def is_empty(self) -> bool: 
        return self.size == 0
    
    #returns size of sequence
    def get_size(self) -> int:
        return self.size
    
    def get_bytes_size(self) -> int:
        return self.bytes_total_size

            
