import pytest
from nltk_utils import tokenize_text, stem_word, bag_of_words
from model_imp import NeuralNet #Importing the class so that we can test the method inside of it
from odessa_chat import get_message
from gui_design import OdessaApplication

#This portion of the project contains official tests for the functions and methods that appear in the code.
#In some of the files, preliminary testing may have been done already, but this file ensures that everything is
#working properly.


#Examples: This portion contains variables needed to test the functions and methods:
ex_sentence_one = "I have a headache."
ex_sentence_two = "I don't have a headache."
ex_sentence_three = "What is the matter?"

def test_tokenize_text():
    assert tokenize_text(ex_sentence_one) == ["I", "have", "a", "headache", "."]
    assert tokenize_text(ex_sentence_two) == ["I", "do", "n't", "have", "a", "headache", "."]
    assert tokenize_text(ex_sentence_three) == ["What", "is", "the", "matter", "?"]
