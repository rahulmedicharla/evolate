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
    <li>Total length of data set</li>
    <li>Insertion/Deletion frequency</li>
    <li>Search Randomness (normalized standard deviation of search pattern)</li>
</ul> 