from data_structures.data_types import DataType, ErrorType
from data_structures.node import Node

#This is the implementation of the Queue using the multipurpose Node.
class Queue():

    """
    Each Queue has these variables

    data (array): This is an array that holds all the data
    size (int) : This holds the size of the queue

    """
    def __init__(self) -> None:
        self.data = []
        self.size = 0
    
    #function to append item to queue
    def enqueue(self, value) -> None:
        self.data.append(Node(self.size, value, DataType.QUEUE))
        self.size+= 1
    
    def dequeue(self) -> Node or ErrorType:
        if self.is_empty() == True:
            return ErrorType.EMPTY_LIST
        
        temp_node = self.data.pop(0)
        self.size -= 1

        return temp_node
    
    def front(self) -> Node or ErrorType:
        if self.is_empty() == True:
            return ErrorType.EMPTY_LIST

        temp_node = self.data[0]
        return temp_node

    #function to iterate through queue and print data
    def iterate(self) -> None:
        for node in self.data:
            node.print_data()

    #returns boolean for if the queue is empty
    def is_empty(self) -> bool: 
        return self.size == 0
    
    #returns size of queue
    def get_size(self) -> int:
        return self.size

            
