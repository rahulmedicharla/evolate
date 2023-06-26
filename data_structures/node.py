#This is the multipurpose class that is going to be used as the base unit of a data structure
from sys import getsizeof
from data_structures.data_types import DataType
class Node:

    """
    Each Node is going to have these values

    key: (int): holds a unique identifier for each node
    value: (T): value can be of any type
    size (int): holds the size of the Node in bytes
    type (DataType): integer value that holds the current implementation of the Nodes

    self.update_value(new_value): This is a function that updates the value of the Node.

    """
    def __init__(self, key: int, value: any, type: DataType) -> None:
        self.key = key
        self.value = value
        self.size = getsizeof(value)
        self.type = type

        #add different parameters based on the current data type implementation
        if self.type == DataType.SINGLY_LINKED_LIST:
            self.next = None
    

    #update_value takes in a param of new value
    def update_value(self, new_value: any) -> None:
        self.value = new_value
        self.size = getsizeof(new_value)

    #print_data prints all the value about the Node
    def print_data(self):
        print("Key: " + str(self.key))
        print("Value: " + str(self.value))
        print("Size: " + str(self.size))
        print("Type: " + str(self.type))

