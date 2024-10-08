import random
import json
import torch
from model_imp import NeuralNet
from nltk_utils import bag_of_words, tokenize_text

#Check for GPU support; this is the same code as before:
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#Open and load the file:
with open('intents.json', 'r') as f:
    intents = json.load(f)

SAVED_FILE = 'various_data_vars.pth'
data = torch.load(SAVED_FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]

all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


#This is where the actual implementation of the chat occurs:
chatbot_name = "Odessa"


#Obtains the message typed by the user and then outputs a response. If Odessa is not able to come up
#with a response for the user, a separate message will appear (see below)
def get_message(message):

    user_dialog = tokenize_text(message)
    modified_sentence = bag_of_words(user_dialog, all_words)
    modified_sentence = modified_sentence.reshape(1, modified_sentence.shape[0])
    modified_sentence = torch.from_numpy(modified_sentence)

    output = model(modified_sentence)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    prob_softmax = torch.softmax(output, dim=1)
    probabilities = prob_softmax[0][predicted.item()]

    if probabilities.item() > 0.75:
        for i in intents["intents"]:
            if tag == i["tag"]:
                return random.choice(i["responses"])

    #Run if Odessa is not able to come up with a response for the user
    else:
        return "I do not understand. Could you please clarify?"
