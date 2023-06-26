from enum import Enum

#enums for the different data types available
class DataType(Enum):
    SINGLY_LINKED_LIST = 0
    QUEUE = 1
    STACK = 2
    SEQUENCE = 3

#different error types available
class ErrorType(Enum):
    NODE_NOT_FOUND = "The Node with the specified key was not found"
    EMPTY_LIST = "This is an empty data structure with no Node and nothing to remove"
    INDEX_OUT_OF_BOUNDS = "Index provided is out of bounds"