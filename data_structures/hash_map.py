"""
This is an implementation of a hash map using the custom multimodal node
"""

from data_types import SubDataStructure, ResponseType, DataType, NodeInterface
from data_structures.node import Node
from sys import getsizeof

class HashMap(SubDataStructure):
    """
    Variables:
        capacity (int): this is the number of buckets that exist
        buckets ([[]]) : this is an array that holds 10 arrays for each bucket
        length (int): this is a counter holding a count of the number of Nodes
        size(int): this is the counter for how many bytes the total length is

    """
    def __init__(self) -> None:
        self.capacity = 10
        self.buckets = [[] for _ in range(self.capacity)]
        self.length = 0
        self.size = 0

        self.idt = 0
        self.ut = 0
        self.st = 0
        self.tc = 0


    """
    ********************************************************************************************************************************************
    the functions below are the ones implemented by SubDataStructure
    """
    def add(self, temp_node: NodeInterface) -> ResponseType:
        self.idt += 1
        self.tc += 1

        index = self.get_hash(temp_node.get_key())
        self.buckets[index].append(temp_node)

        self.length += 1
        self.size += getsizeof(temp_node)

        if self.length >= self.capacity * .7:
            self.resize()

        return ResponseType.SUCCESS

    def remove(self, key: int) -> NodeInterface or ResponseType:
        self.idt += 1
        self.tc += 1

        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        index = self.get_hash(key)
        bucket = self.buckets[index]
        for i, node in enumerate(bucket):
            if node.get_key() == key:
                
                temp_node = bucket[i]
                del bucket[i]
                self.shift_keys_down(temp_node.get_key())
                self.length -= 1
                self.size -= getsizeof(temp_node)                
                return temp_node
            
        return ResponseType.NODE_NOT_FOUND
        
    def get(self, key: int) -> NodeInterface or ResponseType:
        self.st += 1
        self.tc += 1

        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        index = self.get_hash(key)
        bucket = self.buckets[index]
        for i, node in enumerate(bucket):
            if node.get_key() == key:
                temp_node = bucket[i]
                return temp_node
            
            
        return ResponseType.NODE_NOT_FOUND

    def update(self, key: int, value: any) -> ResponseType:
        self.ut += 1
        self.tc += 1
        
        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        node = self.get(key)
        if node == ResponseType.NODE_NOT_FOUND:
            return ResponseType.NODE_NOT_FOUND
        
      
        node.update_value(value)

        return ResponseType.SUCCESS
    
    def get_length(self) -> int:
        return self.length
    
    def get_size(self) -> int:
        return self.size
    
    def iterate(self, iterate_function) -> ResponseType:
        for bucket in self.buckets:
            for node in bucket:
                iterate_function(node)

    def print_metadata(self) -> ResponseType:
        print("Length: " + str(self.length))
        print("Size: " + str(self.size))

        return ResponseType.SUCCESS
    
    def get_insertion_deletion_total(self) -> int:
        return self.idt
    
    def get_update_total(self) -> int:
        return self.ut
    
    def get_commands_total(self) -> int:
        return self.tc
    
    def get_search_total(self) -> int:
        return self.st
    
    
    """
    ********************************************************************************************************************************************
    the functions below are the helper methods
    """

    #function to shift down indexes
    def shift_keys_down(self, removed_key: int) -> ResponseType:
        for bucket in self.buckets:
            for node in bucket:
                if node.get_key() > removed_key:
                    node = self.remove(node.get_key())
                    node.update_key(node.get_key() -1)
                    self.reorient_node(node)

        return ResponseType.SUCCESS

    #function to determine if hashmap is empty
    def is_empty(self) -> bool:
        return self.length == 0

    #function to get hash index of new node
    def get_hash(self, key: int) -> int:
        return hash(key) % self.get_capacity()
    
    #function to get current capacity of index
    def get_capacity(self) -> int:
        return self.capacity
    
    #function to resize bucket if necessary
    def resize(self) -> ResponseType:
        self.capacity *= 2
        new_buckets = [[] for _ in range(self.get_capacity())]
        for bucket in self.buckets:
            for node in bucket:
                index = self.get_hash(node.get_key())
                new_buckets[index].append(node)
        
        self.buckets = new_buckets
        return ResponseType.SUCCESS
    
    def reorient_node(self, node: NodeInterface) -> ResponseType:
        
        index = self.get_hash(node.get_key())
        self.buckets[index].append(node)
        self.length += 1

        return ResponseType.SUCCESS
