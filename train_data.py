import json
from nltk_utils import tokenize_text, stem_word, bag_of_words
import numpy as np
import torch #Needed for dataset creation
import torch.nn as nn #Needed for dataset creation
from torch.utils.data import Dataset, DataLoader #Needed for dataset creation
from model_imp import NeuralNet


#Start off by opening and loading the json file
with open('intents.json', 'r') as f:
    intents = json.load(f)

#Need to set an empty list for all the words we may need; this will be an initial value
all_words = []

#The same will be done with tags and a separate list for patterns AND tags
tags = []
patterns_and_tags = []

for i in intents['intents']:
    tag = i['tag']
    tags.append(tag)
    for p in i['patterns']:
        w = tokenize_text(p)
        all_words.extend(w)
        patterns_and_tags.append((w, tag))

#These are the symbols that our model will ignore
symbols_to_ignore = ["?", "!", ".", ","]
all_words = [stem_word(w) for w in all_words if w not in symbols_to_ignore]
all_words = sorted(set(all_words)) #The sorted function will return a list
tags = sorted(set(tags))
#print(tags)
#print(all_words)

#Although they started as empty lists, X_train and y_train need to be converted
#to arrays (See code after the for loop)
X_train = []
y_train = []
for (pattern_sentence, tag) in patterns_and_tags:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

X_train = np.array(X_train) #Defined training data
y_train = np.array(y_train) #Defined training data

#Dataset is an abstract class. This will allow us to access data points
#and other information
class OdessaDataset(Dataset): #Inherits from Dataset

    #This method gets called when an instance of OdessaDataset is made
    #Serves as our basic constructor
    def __init__(self):
        self.n_samples = len(X_train) #Returns number of samples in dataset, stored in self.n_samples (Instance variable)
        self.x_data = X_train #Attributes training features to self.x_data (Instance variable)
        self.y_data = y_train #Attributes training labels to y_data (Instance variable)

    #Returns a sample from the dataset, including its feature and label, at the passed-in index
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index] #Returns a tuple

    #Returns number of samples in self.n_samples (from basic constructor)
    def __len__(self):
        return self.n_samples


#Hyperparameters:
batch_size = 8 #Number Samples for every batch
hidden_size = 8
dataset = OdessaDataset() #Instance from where we get data
output_size = len(tags)
input_size = len(X_train[0]) #Number of features in input data
learning_rate = 0.001 #Step size for optimizer
num_of_epochs = 100 #Number of passes through training data

#DataLoader portion:
dataloader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)


#Represents our loss function
criterion = nn.CrossEntropyLoss()

#Represents out Adam optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

#Training loop:
for epoch in range(num_of_epochs):
    for (words, labels) in dataloader:
        words = words.to(device)
        labels = labels.to(device, dtype=torch.int64)

        outputs = model(words)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'epoch {epoch + 1} / {num_of_epochs}, loss = {loss.item():.4f}')

print(f'final loss, loss = {loss.item():.4f}')





