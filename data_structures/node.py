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
    
    #function to update value of Node
    def update_value(self, new_value: any) -> ResponseType:
        self.value = new_value

        return ResponseType.SUCCESS
    
    def update_key(self, new_key: int) -> ResponseType:
        self.key = new_key

    def get_key(self) -> int:
        return self.key
        
