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
ex_sentence_four = "I love getting bruises!"
ex_sentence_five = "I do not like headaches, especially after work."
ex_sentence_no_sym = "I have a headache"
ex_sentence_all_sym = "I have leg pain. Do you think I have a strain? If so, let me know!"

ex_word_one = "destroy"
ex_word_two = "Destroyed"
ex_word_three = "destroys"
ex_word_four = "train"
ex_word_five = "trains"
ex_word_six = "Trained"
ex_word_seven = "Ravenhill"


#Tests for the function tokenize_text
def test_tokenize_text():
    assert tokenize_text(ex_sentence_one) == ["I", "have", "a", "headache", "."]
    assert tokenize_text(ex_sentence_two) == ["I", "do", "n't", "have", "a", "headache", "."]
    assert tokenize_text(ex_sentence_three) == ["What", "is", "the", "matter", "?"]
    assert tokenize_text(ex_sentence_four) == ["I", "love", "getting", "bruises", "!"]
    assert tokenize_text(ex_sentence_five) == ["I", "do", "not", "like", "headaches", ",", "especially", "after",
                                               "work", "."]
    assert tokenize_text(ex_sentence_no_sym) == ["I", "have", "a", "headache"]
    assert tokenize_text(ex_sentence_all_sym) == ["I", "have", "leg", "pain", ".", "Do", "you", "think", "I",
                                                  "have", "a", "strain", "?", "If", "so", ",", "let", "me", "know", "!"]


#Tests for the function stem_word
def test_stem_word():
    assert stem_word(ex_word_one) == "destroy"
    assert stem_word(ex_word_two) == "destroy"
    assert stem_word(ex_word_three) == "destroy"
    assert stem_word(ex_word_four) == "train"
    assert stem_word(ex_word_five) == "train"
    assert stem_word(ex_word_six) == "train"
    assert stem_word(ex_word_seven) == "ravenhil"


#Tests for the function bag_of_words
def test_bag_of_words():
    assert 




