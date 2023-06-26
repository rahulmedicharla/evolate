from data_structures.data_types import DataType, ErrorType
from data_structures.node import Node

#This is the implementation of the Stack using the multipurpose Node.
class Stack():

    """
    Each Stack has these variables

    data (array): This is an array that holds all the data
    size (int) : This holds the size of the stack
    bytes_total_size (int): This holds the total size of stack in bytes

    """
    def __init__(self) -> None:
        self.data = []
        self.size = 0
        self.bytes_total_size = 0
    
    #function to append item to stack
    def push(self, value) -> None:
        temp_node = Node(self.size, value, DataType.STACK)
        self.data.append(temp_node)
        self.size+= 1
        self.bytes_total_size += temp_node.size
    
    #function to remove top item in stack
    def pop(self) -> Node or ErrorType:
        if self.is_empty() == True:
            return ErrorType.EMPTY_LIST
        
        temp_node = self.data.pop(self.size-1)
        self.size -= 1
        self.bytes_total_size -= temp_node.size

        return temp_node
    
    #function to show top item in stack
    def peek(self) -> Node or ErrorType:
        if self.is_empty() == True:
            return ErrorType.EMPTY_LIST

        temp_node = self.data[self.size-1]
        return temp_node

    #function to iterate through stack and print data
    def iterate(self) -> None:
        for node in self.data:
            node.print_data()

    #returns boolean for if the stack is empty
    def is_empty(self) -> bool: 
        return self.size == 0
    
    #returns size of stack
    def get_size(self) -> int:
        return self.size
    
    #returns total size of stack in bytes
    def get_bytes_size(self) -> int:
        return self.bytes_total_size


            
