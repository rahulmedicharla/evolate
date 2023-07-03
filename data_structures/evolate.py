"""
 This is the implementation of a the custom modular datatype Evolate

"""
from data_types import DataType, ResponseType, NodeInterface
from data_structures.node import Node
from data_structures.singly_linked_list import SinglyLinkedList
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
    def __init__(self, data_type = DataType) -> None:
        
        self.rep = None
        self.data_type = None

        self.avg_node_size = 0
        self.total_len = 0
        self.total_size = 0
        self.insert_delete_frequency = 0
        self.update_frequency = 0
        self.search_frequency = 0

        #set _rep based on data_type passed in
        if data_type == DataType.SEQUENCE:
            self.rep = Sequence()
            self.data_type = data_type
        elif data_type == DataType.TREE_MAP:
            self.rep = TreeMap()
            self.data_type = data_type
        elif data_type == DataType.HASH_MAP:
            self.rep = HashMap()
            self.data_type = data_type
        else:
            self.rep = SinglyLinkedList()
            self.data_type = DataType.SINGLY_LINKED_LIST


    """
    **************************************************************************************************************
    implementations for six main functions 
    """
    
    def add(self, value: any) -> ResponseType:
        temp_node = Node(self.rep.get_length(), value, self.data_type)
        return self.rep.add(temp_node)
    
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
    
    def get_data_type(self) -> DataType:
        return self.data_type

    def print_items(self) -> ResponseType:
        return self.rep.iterate(self.print)
    
    def print_metadata(self) -> ResponseType:
        return self.rep.print_metadata()
    
    def get_features(self):
        self.avg_node_size = float(self.rep.get_size()) / float(self.rep.get_length())
        self.total_len = self.rep.get_length()
        self.total_size = self.rep.get_size()
        print(self.rep.get_insertion_deletion_total())
        self.insert_delete_frequency = float(self.rep.get_insertion_deletion_total()) / float(self.rep.get_commands_total())
        self.update_frequency = float(self.rep.get_update_total()) / float(self.rep.get_commands_total())
        self.search_frequency = float(self.rep.get_search_total()) / float(self.rep.get_commands_total())

        return self.avg_node_size, self.total_len, self.total_size, self.insert_delete_frequency, self.update_frequency, self.search_frequency

    def print(self, node: NodeInterface) -> ResponseType:
        print("Key: " + str(node.key))
        print("Value: " + str(node.value))
        print("Size: " + str(node.size))
        print("Type: " + str(node.type))
        return ResponseType.SUCCESS
    
    def switch_data_structures(self, new_type: DataType) -> ResponseType:
        #create new data instance
        if new_type == DataType.SEQUENCE:
            new_rep = Sequence()
            self.data_type = new_type
        elif new_type == DataType.TREE_MAP:
            new_rep = TreeMap()
            self.data_type = new_type
        elif new_type == DataType.HASH_MAP:
            new_rep = HashMap()
            self.data_type = new_type
        elif new_type == DataType.SINGLY_LINKED_LIST:
            new_rep = SinglyLinkedList()
            self.data_type = DataType.SINGLY_LINKED_LIST

        index = self.rep.get_length() -1
        while index >= 0:
            node = self.rep.get(index)
            new_node = Node(node.get_key(), node.get_value(), self.data_type)
            new_rep.add(new_node)
            index -= 1
        self.rep = new_rep
        return ResponseType.SUCCESS