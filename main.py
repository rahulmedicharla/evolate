from data_structures.evolate import Evolate
import random
from data_types import DataType

list = Evolate(DataType.SEQUENCE)

for i in range(0,100):
    list.add(i)

list.remove(0)

for _ in range(0,1000):
    index = random.randint(0,10)
    list.get(index)

    