"""
 This is the implementation of a the custom modular datatype Evolate

"""
from data_types import DataType, ResponseType, NodeInterface, EvolateNetwork
from data_structures.node import Node
from data_structures.singly_linked_list import SinglyLinkedList
from data_structures.sequence import Sequence
from data_structures.tree_map import TreeMap
from data_structures.hash_map import HashMap

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class Evolate():

    """
    Params:
        -> data_type (DataType) this is a initializer var that tells which data type to use intiially
    
    Var
        -> rep (SubDataStructure): this is the current representation of the data 

    """
    def __init__(self, data_type = DataType.SINGLY_LINKED_LIST) -> None:
        
        self.rep = None
        self.data_type = None

        self.model = EvolateNetwork()
        self.model.load_state_dict(torch.load("machine_learning/weights.pt", map_location=torch.device('cpu')))
        self.model.eval()

        """
        realtime features to keep track of
            -> total length: total length of the dataset
            -> insertion deletion frequency: 0-1 ratio of how many insertion & deletion commands there are
            -> search prediction: 0-1 ratio of average search index
            -> search randomness: -.25 - .25 ratio of how random the search indexes are. Negative means patterened, positive means random

        """
        self.insertion_deletion_frequency = 0
        self.search_prediction = 0
        self.search_randomness = 0

        self.total_commands = 0
        self.idt_commands = 0
        self.search_list = np.array([])

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
        self.total_commands += 1
        self.idt_commands += 1

        self.determine_when_to_switch()

        temp_node = Node(self.rep.get_length(), value, self.data_type)
        return self.rep.add(temp_node)
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        self.total_commands += 1
        self.idt_commands += 1
        self.search_list = np.append(self.search_list, key)

        self.determine_when_to_switch()

        return self.rep.remove(key)
    
    def get(self, key: int) -> NodeInterface or ResponseType:
        self.total_commands += 1
        self.search_list = np.append(self.search_list, key)

        self.determine_when_to_switch()

        return self.rep.get(key)

    def update(self, key: int, value: any) -> ResponseType:
        self.total_commands += 1
        self.search_list = np.append(self.search_list, key)

        self.determine_when_to_switch()

        return self.rep.update(key, value)

    def get_length(self) -> int:
        return self.rep.get_length()
    
    def get_size(self) -> int:
        return self.rep.get_size()
    
    def get_data_type(self) -> DataType:
        return self.data_type
    
    def get_features(self) -> tuple:
        self.insertion_deletion_frequency = round((float(self.idt_commands) / float(self.total_commands)), 3)

        if len(self.search_list) == 0:
            self.search_prediction = 0
            self.search_randomness = 0
        else:
            self.search_prediction = np.average(self.search_list)
            std_dev = np.std(self.search_prediction)
            self.search_randomness = round((float(std_dev) / float(self.rep.get_length())), 3) or 0

        return [int(self.get_size()), float(self.insertion_deletion_frequency), float(self.search_randomness), int(self.search_prediction)]
    
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
    
    def determine_when_to_switch(self):
        if self.total_commands % 100 == 0 and self.total_commands != 0:
            self.evaluate_features()
    
    def evaluate_features(self) -> ResponseType:
        features = torch.tensor(self.get_features())
        with torch.no_grad():
            prediction = self.model(features)
            prediction = F.softmax(prediction, dim = 0)
            
            data_type = DataType.SINGLY_LINKED_LIST
            max = prediction[0]
            if prediction[1] > max:
                data_type = DataType.SEQUENCE
                max = prediction[1]
            if prediction[2] > max:
                data_type = DataType.TREE_MAP
                max = prediction[2]
            if prediction[3] > max:
                data_type = DataType.HASH_MAP
                max = prediction[3]
            
            if data_type != self.data_type:
                self.switch_data_structures(data_type)
                self.data_type = data_type

    
    def switch_data_structures(self, new_type: DataType) -> ResponseType:
        #create new data instance
        print("Switching Data Structure from " + str(self.data_type) + " to " + str(new_type))
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