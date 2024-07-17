import nltk
import numpy as np
#nltk.download('punkt') #Commented out once downloaded; works in conjunction with nltk library
from nltk.stem.porter import PorterStemmer #Needed for stem method

#Make sure you are using conda for the interpreter

#This file will include the three most crucial methods that will be utilized by the chatbot to identify, split up, and
#come up with responses.

#We need a stemmer for stem method:
stemmer = PorterStemmer()

#Returns a tokenized version of the passed-in sentence; tokenization separates a string into individual sections,
#with words, punctuation, and other symbols represented within their own set of ""
def tokenize_text(sentence):
    return nltk.word_tokenize(sentence)


#Generates the root form of words
def stem_word(word):
    return stemmer.stem(word.lower()) #Will make things easier by making all words lowercase


#Adds in a 0.0 or 1.0 depending on if the tokenized word lies within all words. If it does, then a 1.0 is applied;
#if not, then 0.0 is applied. The final array/list will be as long as the all_words parameter.
def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem_word(w) for w in tokenized_sentence] #Stemmer is being applied to each word in the
    #tokenized sentence

    #Each word is initialized with 0 in the bag
    bag = np.zeros(len(all_words), dtype=np.float32)
    for i, w in enumerate(all_words): #i deals with indices, while w deals with individual words in all_words
        if w in tokenized_sentence:
            bag[i] = 1.0

    #The final answer should be as long as all_words
    return bag








#Tests and Examples for the functions above:

#Examples:
a = "I like to eat pizza."
b = "why Is MY brother not HERE?"
c = "pizza"
d = "prepared"
e = "Review"
f = "Aren't"
g = "Can you pay me $20.00?"


#Tests for tokenize:
#print(tokenize_text(a))
#print(tokenize_text(b))
#print(tokenize_text(f))
#print(tokenize_text(g))


#Tests for stem:
#print(stem(c))
#print(stem(d))
#print(stem(e))

word_list = ["Prepared", "Prepare", "Prepares"]
stem_list = [stem_word(w) for w in word_list]
#print(stem_list)


#Tests for bag_of_words:
test_all_words = ["i", "like", "to", "dance", "with", "you", "!"] #Should be lowercase
example_sentence = ["i", "eat", "pizza", "with", "sam", "."] #Should also be lowercase
print(bag_of_words(example_sentence, test_all_words))

