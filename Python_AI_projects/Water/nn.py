import pandas as pd
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split as train_test_split

#device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

water_df = pd.read_csv('/Users/stanloosmore/Documents/Projects/Projects/Water/Water Potability.csv')

water_df = water_df.dropna()

X = water_df.drop(columns='Potability')
y = water_df['Potability']

batch_size = 100

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Assuming X_train is your pandas DataFrame
X_train_np = X_train.to_numpy(dtype=np.float32)  # Convert to NumPy array with the desired data type

# Create a PyTorch tensor from the NumPy array
X_train_t = torch.tensor(X_train_np, dtype=torch.float32)

# Do the same for y_train
y_train_np = y_train.to_numpy(dtype=np.float32)
y_train_t = torch.tensor(y_train_np, dtype=torch.float32)

train_data = torch.utils.data.TensorDataset(X_train_t, y_train_t)
train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)

input_size = 9 
output_layer = 1
epochs = 100

class Net(nn.Module):
    def __init__(self, input_layer, output_layer):
      super(Net, self).__init__()

      self.relu = nn.ReLU()
      self.sig = nn.Sigmoid()

      # First fully connected layer
      self.fc1 = nn.Linear(input_layer, 1024)
      self.fc2 = nn.Linear(1024, 256)
      self.fc3 = nn.Linear(256, 64)
      self.fc4 = nn.Linear(64, 8)
      self.fc5 = nn.Linear(8, output_layer)
    
    def forward(self, input):
      x = self.fc1(input)
      x = self.relu(x)

      x = self.fc2(x)
      x = self.relu(x)

      x = self.fc3(x)
      x = self.relu(x)

      x = self.fc4(x)
      x = self.relu(x)

      x = self.fc5(x)
      x = self.sig(x)
      return x
model = Net(input_size, output_layer)
#print(model)
loss_fuction = torch.nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

total_steps = len(train_loader)
for epoch in range(epochs):
  for i, (attributes, labels) in enumerate(train_loader):

    output = model.forward(attributes)
    loss = loss_fuction(torch.squeeze(output), labels)

    optimizer.zero_grad() 
    loss.backward() 
    optimizer.step() 
    if (i+1) % 100 == 0:
      print(f'epoch {epoch+1} / {epochs}, step {i+1}/{total_steps}, loss = {loss.item():.4f}')