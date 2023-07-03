"""
This is an implementation of a binary search tree using Tree Map
"""

from data_types import SubDataStructure, ResponseType, DataType, NodeInterface
from data_structures.node import Node
from sys import getsizeof

class TreeMap(SubDataStructure):
    """
    Variables:
        root (Node): this is the root node for a tree map
        length (int): this is a counter holding a count of the number of Nodes
        size(int): this is the counter for how many bytes the total length is

    """
    def __init__(self) -> None:
        self.root = None
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
        
        self.root = self.insert(self.root, temp_node)

        self.length += 1
        self.size += getsizeof(temp_node)

        return ResponseType.SUCCESS
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        self.idt += 1
        self.tc += 1

        removed_node = self.get(key)
        if removed_node == ResponseType.NODE_NOT_FOUND or removed_node == ResponseType.EMPTY_LIST:
            return removed_node
        
        temp_node = Node(removed_node.get_key(), removed_node.get_value(), DataType.TREE_MAP)
        self.root = self.remove_recursive(self.root, key)

        self.length -= 1
        self.size -= getsizeof(temp_node)

        return temp_node
        

    def get(self, key: int) -> NodeInterface or ResponseType:
        self.st += 1
        self.tc += 1

        if self.is_empty():
            return ResponseType.EMPTY_LIST
        
        return self.find(self.root, key)

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
        
        self.iterate_recursive(self.root, iterate_function)

        return ResponseType.SUCCESS
    
    def print_metadata(self) -> ResponseType:
        print("Length: " + str(self.length))
        print("Size: " + str(self.size))

        return ResponseType.SUCCESS

    def get_insertion_deletion_total(self) -> int:
        return self.idt
    
    def get_update_total(self) -> int:
        return self.ut
    
    def get_search_total(self) -> int:
        return self.st
    
    def get_commands_total(self) -> int:
        return self.tc
    
    """
    ********************************************************************************************************************************************
    the functions below are the helper methods
    """

    #returns bool for is the singly linked list is empty
    def is_empty(self) -> bool:
        return self.root == None
    
    #recursive implementation of insert
    def insert(self, current: NodeInterface, node: NodeInterface) -> NodeInterface:
        if not current:
            return node
        elif node.get_key() < current.get_key():
            current.left = self.insert(current.left, node)
        else:
            current.right = self.insert(current.right, node)

        
        current.set_height(1 + max(self.get_node_height(current.left), self.get_node_height(current.right)))
        balance_factor = self.get_balance_factor(current)

        if balance_factor > 1:
            if node.get_key() < current.left.get_key():
                return self.rotate_right(current)
            else:
                current.left = self.rotate_left(current.left)
                return self.rotate_right(current)
            
        if balance_factor < -1:
            if node.get_key() > current.right.get_key():
                return self.rotate_left(current)
            else:
                current.right = self.rotate_right(current.right)
                return self.rotate_left(current)
        
        return current

    def find(self, current: NodeInterface, key: int) -> NodeInterface or ResponseType:
        if current == None:
            return ResponseType.NODE_NOT_FOUND
        
        if current.get_key() == key:
            return current
        
        if key < current.get_key():
            return self.find(current.left, key)
        else:
            return self.find(current.right, key)
        
    #a recursive way to remove a node
    def remove_recursive(self, current: NodeInterface, key: int) -> NodeInterface:
            if not current:
                return current
            elif key < current.get_key():
                current.left = self.remove_recursive(current.left, key)
            elif key > current.get_key():
                current.right = self.remove_recursive(current.right, key)
            else:
                if current.left == None:
                    temp = current.right
                    current = None
                    return temp
                elif current.right == None:
                    temp = current.left
                    current = None
                    return temp
                
                temp = self.get_mini_value_node(current.right)
                self.shift_keys_down(current, temp)
                current.right = self.remove_recursive(current.right, temp.get_key())
            
            if current == None:
                return current
            
            current.set_height(1 + max(self.get_node_height(current.left), self.get_node_height(current.right)))
            balance_factor = self.get_balance_factor(current)

            if balance_factor > 1:
                if self.get_balance_factor(current.left) >= 0:
                    return self.rotate_right(current)
                else:
                    current.left = self.rotate_left(current.left)
                    return self.rotate_right(current)
            if balance_factor < -1:
                if self.get_balance_factor(current.right) <= 0:
                    return self.rotate_left(current)
                else:
                    current.right = self.rotate_right(current.right)
                    return self.rotate_left(current)
            
            return current
             
                
    #shifts the keys of the Nodes down when item is removed
    def shift_keys_down(self, current: NodeInterface, temp_node: NodeInterface) -> ResponseType:
        current.update_value(temp_node.get_value())
        return ResponseType.SUCCESS

    #iterate through all nodes recursive
    def iterate_recursive(self, current: NodeInterface, iterate_function) -> None:
        if current:
            self.iterate_recursive(current.left, iterate_function)
            iterate_function(current)
            self.iterate_recursive(current.right, iterate_function)

    #get the height of a node
    def get_node_height(self, node: NodeInterface) -> int:
        if not node:
            return 0
        return node.get_height()

    #get balance factor
    def get_balance_factor(self, node: NodeInterface) -> int:
        if not node:
            return 0
        return self.get_node_height(node.left) - self.get_node_height(node.right)

    #rotate tree map right
    def rotate_right(self, z: NodeInterface) -> NodeInterface:
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.set_height(1 + max(self.get_node_height(z.left), self.get_node_height(z.right)))
        y.set_height(1 + max(self.get_node_height(y.left), self.get_node_height(y.right)))

        return y

    #rotate tree map left
    def rotate_left(self, z: NodeInterface) -> NodeInterface:
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.set_height(1 + max(self.get_node_height(z.left), self.get_node_height(z.right)))
        y.set_height(1 + max(self.get_node_height(y.left), self.get_node_height(y.right)))

        return y
    
    def get_mini_value_node(self, root: NodeInterface) -> NodeInterface:
        if root == None or root.left == None:
            return root
        return self.get_mini_value_node(root.left)
