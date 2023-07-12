## Evolate: the first ever multistructered dynamic data structure

The idea behind evolate is that data is always changing. When the average person uses a data structure in their program, they usually aren't
considering the implications that structure could have on your CPU, Memory, or Efficiency. Certain features of the data your storing, your use case, and the search algorithms you chose to use may cause your structure be inefficent. 
<br>
Evolate solves the problem using ML. Evolate keeps track of the features of the data you're storing and based on custom trained model, it will automatically switch between different data implementations, which use different search algorithms to maximize efficiency while minimizing stress on your PC. 

<h3>Data Structures Evolate uses and switches between:</h3>
<ul>
    <li>Singly Linked List</li>
    <ul>
        <li>Uses Iterative Search <i>Runtime: Θ(n)</i></li>
        <li>Uses Iterative Insertion & Deletion <i>Runtime: Θ(n)</i></li>
    </ul>
    <li>Sequence</li>
    <ul>
        <li>Uses Iterative Binary Search <i>Runtime: Θ(log(n))</i></li>
        <li>Uses Iterative Insertion & Deletion <i>Runtime: Θ(n)</i></li>
    </ul>
    <li>Tree Map</li>
    <ul>
        <li>Uses Recursive Binary Search <i>Runtime: Θ(log(n))</i></li>
        <li>Uses Iterative Insertion & Deletion <i>Runtime: Θ(log(n))</i></li>
    </ul>
    <li>Hash Map</li>
    <ul>
        <li>Uses Hashed Search <i>Runtime: Θ(1)</i></li>
        <li>Uses Hashed Insertion & Deletion <i>Runtime: Θ(1)</i></li>
    </ul>
</ul>
  
<br>
The runtimes provided are in the general case of the data set. However, certain data structures operate better based on specifications for the data.
<ul>
    <li>Singly Linked List</li>
    <ul>
        <li><i>Advantanges:</i> Efficient search at head of list & constant insertion/deletion</li>
        <li><i>Disadvantages:</i> Slow search at end of list</li>
    </ul>
    <li>Sequence</li>
    <ul>
       <li><i>Advantanges:</i> Efficient random search  & constant insertion/deletion</li>
       <li><i>Disadvantages:</i> Inefficient for search patterns</li>
    </ul>
    <li>Tree Map</li>
    <ul>
       <li><i>Advantanges:</i> Fast random search for smaller data sets (Memory Extensive)</li>
       <li><i>Disadvantages:</i> Slow insertion/deletion (need to maintain balanced tree)</li>
    </ul>
    <li>Hash Map</li>
    <ul>
         <li><i>Advantanges:</i> Fast insertion/deletion & search</li>
         <li><i>Disadvantages:</i> Not good for very large data sets</li>
    </ul>
</ul>

<h3>Machine Learning</h3>

<b>Based on the specifications for the data, these were the features I chose to keep track of in real time</b>
<ul>
    <li>Size of data set in bytes</li>
    <li>Insertion/Deletion frequency</li>
    <li>Search Randomness (normalized standard deviation of search pattern)</li>
    <li>Search Prediction (index that is most commonly searched)</li>
</ul> 

To generate the data, I created a file to generate random values for these four features, and run the number of insertions/deletions/searches to attain those values. I did for all four data types and recorded the one
with the shortest run time. 

Here is a visualization of a small piece of the data the ML model is trained on.
<img src = "https://github.com/rahulmedicharla/evolate/blob/31bcba7c53fa796f07f0e96ee6887918cd6941fb/readme_images/visualization.png" alt="Data IMG"></img>

As you can see the data is no where linear. Using the pytorch library, I created a custom Neural Network that would be able to understand the non linear patterns within this data.

After implementing within Evolate, it's now able to run an inference every 500 commands with the modified realtime features to determine whether to switch data structures, and will do so if necessary.

<h3>How to use evolate</h3>
<ol>
    <li>Clone repository into your local directory</li>
    <li>Create a virtual environment named 'venv'</li>
    <li>Activate virtual environment and install 'requirements.txt'</li>
    <li>Open main.py and use as you please!</li>
</ol>

Here are some examples to get started

```
from data_structures.evolate import Evolate
from data_types import DataType, NodeInterface

list = Evolate()

#you can also specify initial data type implementation
# list = Evolate(DataType.SINGLY_LINKED_LIST)
# list = Evolate(DataType.TREE_MAP)
# list = Evolate(DataType.HASH_MAP)
# list = Evolate(DataType.SEQUENCE)

#there are five main functions you can do with evolate

# evolate.add(value :any)
list.add(0)
list.add("Hello World")
list.add({
    'name': 'first element!',
    'value':  'value one!'
})

#evolate.remove(key : int) -> Node
#evolate follows standard array indexing from range(0,n) for range(0,n-1)
list.remove(0) -> "0"
list.remove(0) -> "Hello World"

#evolate.get(key : int) -> Node
list.get(0) -> "0"
list.get(1) -> "Hello World"

#evolate.update(key: int, value: any)
list.update(0, 1)
list.get(0) -> "1"

```

