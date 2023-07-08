"""
 This is a interface file that holds the enums and interfaces for the datatypes and structures that exist

"""

from enum import Enum
from abc import ABC, abstractmethod
import torch
import torch.nn as nn
import torch.nn.functional as F

class EvolateNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.input = nn.Linear(3, 6).to(self.device)
        self.h1 = nn.Linear(6,8).to(self.device)
        self.h2 = nn.Linear(8,8).to(self.device)
        self.h3 = nn.Linear(8,6).to(self.device)
        self.output = nn.Linear(6,4).to(self.device)

    def forward(self, x):
        x = F.relu(self.input(x.to(self.device)))
        x = F.relu(self.h1(x.to(self.device)))
        x = F.relu(self.h2(x.to(self.device)))
        x = F.relu(self.h3(x.to(self.device)))
        return self.output(x.to(self.device))


#ENUMS for data types
class DataType(Enum):
    SINGLY_LINKED_LIST = 0
    SEQUENCE = 1
    TREE_MAP = 2
    HASH_MAP = 3

#ENUMS for error types
class ResponseType(Enum):
    SUCCESS = "Succces"
    NODE_NOT_FOUND = "The node with specified key was not found"
    EMPTY_LIST = "The data structure is empty"


#abstract class for a universal multiNode
class NodeInterface(ABC):
    #init function to create a Node
    @abstractmethod
    def __init__(self, key: int, value: any, type: DataType) -> None:
        pass

    #function to update value of node
    @abstractmethod
    def update_value(self, new_value : any) -> ResponseType:
        pass

    #function to update keys of node
    @abstractmethod
    def update_key(self, new_key: int) -> ResponseType:
        pass

    #function get key of node
    @abstractmethod
    def get_key(self) -> int:
        pass

    #function to get value of node
    @abstractmethod
    def get_value(self) -> any:
        pass

    #function to get height of a Tree Map Node
    @abstractmethod
    def get_height(self) -> int:
        pass

    #function set height of a Tree Map node
    @abstractmethod
    def set_height(self, new_height: int) -> ResponseType:
        pass

    #function to print items of node
    @abstractmethod
    def print(self) -> None:
        pass

#abstract class for every sub data structure
class SubDataStructure(ABC):
    
    #add Node to data structure
    @abstractmethod
    def add(self, temp_node: NodeInterface) -> ResponseType:
        pass

    #remove Node from data structure with specified key
    @abstractmethod
    def remove(self, key: int) -> NodeInterface or ResponseType:
        pass

    #get value of Node with specific key
    @abstractmethod
    def get(self, key: int) -> NodeInterface or ResponseType:
        pass

    #update value of Node with specific key
    @abstractmethod
    def update(self, key: int, value : any) -> ResponseType:
        pass

    #get length of data structure, # of Nodes
    @abstractmethod
    def get_length(self) -> int:
        pass

    #get size of data structure in bytes
    @abstractmethod
    def get_size(self) -> int:
        pass

    #an iterate function that passed in a function pointer passes each node to that function
    @abstractmethod
    def iterate(self, iterate_function) -> ResponseType:
        pass

    #an simple function to get meta data about external structure
    @abstractmethod
    def print_metadata(self) -> ResponseType:
        pass