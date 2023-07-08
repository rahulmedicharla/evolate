import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from IPython import display

class EvolateNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.input = nn.Linear(3, 6).to(self.device)
        self.h1 = nn.Linear(6,8).to(self.device)
        self.h2 = nn.Linear(8,8).to(self.device)
        self.h3 = nn.Linear(8,6).to(self.device)
        self.output = nn.Linear(6,4).to(self.device)

    def forward(self, x):
        x = F.relu(self.input(x.to(self.device)))
        x = F.relu(self.h1(x.to(self.device)))
        x = F.relu(self.h2(x.to(self.device)))
        x = F.relu(self.h3(x.to(self.device)))
        return self.output(x.to(self.device))

def load_data(file_path) -> tuple:
    #read data, create cross
    df = pd.read_csv(file_path)
    data_structures = torch.tensor(
        [0 if ds == "SINGLY_LINKED_LIST" else 1 if ds == "SEQUENCE" else 2 if ds == "TREE_MAP" else 3 for ds in df["Data Structure"]],
        dtype=torch.long
    )
    df = df.drop("Size", axis=1)
    features = torch.tensor(df.iloc[: ,:3].values, dtype=torch.float)
    return features, data_structures

def split_data(features, data_structures) -> tuple:
    features_train, features_test, ds_train, ds_test = train_test_split(features, data_structures, train_size=.8, random_state=42)

    train_data = TensorDataset(features_train, ds_train)
    test_data = TensorDataset(features_test, ds_test)

    train_loader = DataLoader(train_data, shuffle=True, batch_size=50)
    test_loader = DataLoader(test_data, batch_size=len(test_data.tensors[0]))

    return train_loader, test_loader

def train_model(train_loader, test_loader, model, device):
    num_epochs = 10
    train_accuracies, test_accuracies = [], []

    loss_function = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(params=model.parameters(), lr=0.0001)

    for epoch in range(num_epochs):
        print("Epoch: " + str(epoch))
        # Train set
        for X, y in train_loader:
            X = X.to(device)
            y = y.to(device)

            preds = model(X)
            pred_labels = torch.argmax(preds, axis=1)

            loss = loss_function(preds, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        train_accuracies.append(
            100 * torch.mean((pred_labels == y).float()).item()
        )
        
        # Test set
        X, y = next(iter(test_loader))
        pred_labels = torch.argmax(model(X.to(device)), axis=1)
        test_accuracies.append(
            100 * torch.mean((pred_labels.to(device) == y.to(device)).float()).item()
        )

    return train_accuracies, test_accuracies

def main():
    features, data_structures = load_data("machine_learning/data/data.csv")
    train_loader, test_loader = split_data(features, data_structures)

    model = EvolateNetwork() 
    model.to(model.device)
    display.set_matplotlib_formats("svg")

    train_accuracies, test_accuracies = train_model(train_loader, test_loader, model, model.device)
    torch.save(model.state_dict(), "machine_learning/weights.pt")

    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(nrows=2, ncols=1)

    ax = fig.add_subplot(gs[0, 0])
    ax.plot(train_accuracies)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Training accuracy")

    ax = fig.add_subplot(gs[1, 0])
    ax.plot(test_accuracies)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Test accuracy")

    fig.align_labels()
    plt.show()

if __name__ == '__main__':
    main()