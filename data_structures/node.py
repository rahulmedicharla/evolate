"""
This is the implementation for a custom multi datastructure Node
"""

from sys import getsizeof
from data_types import NodeInterface, DataType, ResponseType

class Node(NodeInterface):

    """
    Params
        -> key (int): a unique key index for each Node
        -> value (any): the Value to be stored in Node
        -> type (DataType): information about the  

    Variables
        -> key, value, type
        -> size (int): holds information on how many bytes a Node is
    
    """
    def __init__(self, key: int, value: any, type: DataType) -> None:
        self.key = key
        self.value = value
        self.type = type
        self.size = getsizeof(value)

        #specific variables for data type implementation
        if self.type == DataType.SINGLY_LINKED_LIST:
            self.next = None
        
        if self.type == DataType.TREE_MAP:
            self.left = None
            self.right = None
            self.height = 1
    
    #function to update value of Node
    def update_value(self, new_value: any) -> ResponseType:
        self.value = new_value

        return ResponseType.SUCCESS
    
    def update_key(self, new_key: int) -> ResponseType:
        self.key = new_key

    def get_key(self) -> int:
        return self.key
    
    def get_value(self) -> any:
        return self.value
    
    def get_height(self) -> int:
        return self.height
    
    def set_height(self, new_height: int) -> ResponseType:
        self.height = new_height
        return ResponseType.SUCCESS
    
    def print(self):
        print("Key: " + str(self.key))
        print("Value: " + str(self.value))
        print("Size: " + str(self.size))
        print("Type: " + str(self.type))
