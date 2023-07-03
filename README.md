## Evolate: the first ever multistructered dynamic data structure

The idea behind evolate is that data is always changing. When the average person uses a data structure in their program, they usually aren't
considering the implications that structure could have on your CPU, Memory, or Efficiency. Certain features of the data your storing, your use case, and the search algorithms you chose to use may be inefficent. 

Evolate solves the problem using ML. Evolate keeps track of the features of the data you're storing and based on custom trained model, it will automatically switch between different data implementations, which use different search algorithms to maximize efficiency while minimizing stress on your PC. 

<b>Data Structures Evolate can use:</b>
    -> Singly Linked List
        -> Uses iterative search approach
    -> Sequence:
        -> Ordered List: implements binary search
    -> Tree Map : binary search tree implementation
        -> Uses DFS
    -> Hash Map
        -> Uses hash algorithm search approach

<b>ML: keeps track of the properties of the current data set and uses them to predict when to change data structures</b>
Features to keep Track of: 
    -> Average Size of node (bytes)
    -> Total Size of Node (bytes)
    -> Total length of node (len of data set)
    -> Insertion/Deletion frequency (0-1 ratio of how much insertion/deletion there is compared to total commands)
    -> Update frequency (0-1 ratios of how much update there is compared to total commands)