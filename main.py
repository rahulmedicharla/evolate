from data_structures.evolate import Evolate
from data_types import DataType

list = Evolate(DataType.TREE_MAP)

list.add("value1")
list.add("value2")
list.add("value3")

node = list.remove(1)

print(node.get_value())