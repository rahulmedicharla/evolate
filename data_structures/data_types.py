from enum import Enum

class DataType(Enum):
    SINGLY_LINKED_LIST = 0

class ErrorType(Enum):
    NODE_NOT_FOUND = "The Node with the specified key was not found"
    EMPTY_LIST = "This is an empty list nothing to remove"