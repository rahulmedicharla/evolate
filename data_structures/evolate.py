"""
 This is the implementation of a the custom modular datatype Evolate

"""
from data_types import DataType, ResponseType, NodeInterface
from data_structures.singly_linked_list import SinglyLinkedList
from data_structures.queue import Queue
from data_structures.sequence import Sequence
from data_structures.tree_map import TreeMap
from data_structures.hash_map import HashMap

class Evolate():

    """
    Params:
        -> data_type (DataType) this is a initializer var that tells which data type to use intiially
    
    Var
        -> rep (SubDataStructure): this is the current representation of the data 

    """
    def __init__(self, data_type: DataType) -> None:
        
        self.rep = None

        #set _rep based on data_type passed in
        if data_type == DataType.SINGLY_LINKED_LIST:
            self.rep = SinglyLinkedList()
        elif data_type == DataType.QUEUE:
            self.rep = Queue()
        elif data_type == DataType.SEQUENCE:
            self.rep = Sequence()
        elif data_type == DataType.TREE_MAP:
            self.rep = TreeMap()
        elif data_type == DataType.HASH_MAP:
            self.rep = HashMap()


    """
    **************************************************************************************************************
    implementations for six main functions 
    """
    
    def add(self, value: any) -> ResponseType:
        return self.rep.add(value)
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        return self.rep.remove(key)
    
    def get(self, key: int) -> NodeInterface or ResponseType:
        return self.rep.get(key)

    def update(self, key: int, value: any) -> ResponseType:
        return self.rep.update(key, value)

    def get_length(self) -> int:
        return self.rep.get_length()
    
    def get_size(self) -> int:
        return self.rep.get_size()


    def print_items(self) -> ResponseType:
        return self.rep.iterate(self.print)
    
    def print_metadata(self) -> ResponseType:
        return self.rep.print_metadata()
    
    def print(self, node: NodeInterface) -> ResponseType:
        print("Key: " + str(node.key))
        print("Value: " + str(node.value))
        print("Size: " + str(node.size))
        print("Type: " + str(node.type))
        return ResponseType.SUCCESS
    
