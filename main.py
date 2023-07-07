from data_structures.evolate import Evolate

list = Evolate()

for i in range(0,1000):
    list.add(i)

for i in range(0,100):
    list.get(i)


# from data_types import EvolateNetwork
# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import numpy as np

# model = EvolateNetwork()
# model.load_state_dict(torch.load("machine_learning/weights.pt", map_location=torch.device('cpu')))
# model.eval()

# with torch.no_grad():
#     a = 0
#     b = 0.0
#     c = 0.0
#     d = 0
#     print(type(b))
#     data = torch.tensor([a,b,c,d])
#     res = model(data)
#     output = F.softmax(res, dim=0)
#     print(output)

