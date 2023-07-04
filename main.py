from data_structures.evolate import Evolate
from data_types import DataType

list = Evolate(DataType.HASH_MAP)

list.add(0)
list.add(1)
list.add(2)
list.add(3)
list.add(4)
list.add(5)
list.add(6)
list.add(7)
list.add(8)
list.add(9)
list.add(10)
list.add(11)
list.add(12)
list.add(13)
list.add(14)
list.add(15)
list.add(16)
list.add(17)
list.add(18)
list.add(19)

list.get(0)
list.get(19)

features = list.get_features()

print(features)
