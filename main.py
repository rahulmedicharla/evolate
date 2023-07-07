import torch
from data_types import EvolateNetwork

model = EvolateNetwork()
model.load_state_dict(torch.load("machine_learning/weights.pt", map_location=torch.device('cpu')))

model.eval()

with torch.no_grad():
    data = torch.tensor([0,0.0,0.0,0])
    out_data = model(data)
    print(out_data)
    data = torch.tensor([0,0.2345,0.23456,0])
    out_data = model(data)
    print(out_data)