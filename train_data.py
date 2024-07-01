import json
from nltk_utils import tokenize_text, stem_word, bag_of_words

#Start off by opening and loading the json file
with open('intents.json', 'r') as f:
    intents = json.load(f)

#print(intents)

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

symbols_to_ignore = ["?", "!", ".", ","]
all_words = [stem_word(w) for w in all_words if w not in symbols_to_ignore]
all_words = sorted(set(all_words)) #The sorted function will return a list
tags = sorted(set(tags))
#print(tags)

X_train = []
y_train = []
for (pattern_sentence, tag) in patterns_and_tags:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

#Once this portion is finished, the tags that are in the json file will be listed
#in alphabetical order in the console window (the print statement allowing that to
# happen has been commented out since it was just a test).











