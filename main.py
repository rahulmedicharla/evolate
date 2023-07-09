from data_structures.evolate import Evolate
import random
from data_types import DataType

list = Evolate(DataType.TREE_MAP)


for i in range(0,1000):
    list.add(i)

for _ in range(0,100):
    index = random.randint(0, list.get_length())
    list.remove(index)