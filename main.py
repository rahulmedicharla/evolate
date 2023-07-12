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
list.remove(0)
list.remove(0) 
#evolate.get(key : int) -> Node
list.get(0) 
list.get(1) 
#evolate.update(key: int, value: any)
list.update(0, 1)
list.get(0) 
