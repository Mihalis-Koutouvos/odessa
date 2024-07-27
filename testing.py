import pytest
import torch
import torch.nn as nn
import unittest.mock import patch
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
ex_all_words = ["hello", "i", "have", "do", "a", "headache", "?", ".", "so", "if", "why", "not", "matter", "like",
                "strain", "bruise", "pneumonia", "concussion", "happy", "sad", "pain", ",", "after", "work"]

ex_word_one = "destroy"
ex_word_two = "Destroyed"
ex_word_three = "destroys"
ex_word_four = "train"
ex_word_five = "trains"
ex_word_six = "Trained"
ex_word_seven = "Ravenhill"

ex_tokenized_text_one = ["i", "have", "a", "headache", "."]
ex_tokenized_text_two = ["i", "do", "not", "have", "a", "headache", ",", "especially", "after", "work", "."]





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
                                                  "have", "a", "strain", "?", "If", "so", ",", "let", "me",
                                                  "know", "!"]


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
#list(input) ensures that there is no ValueError
def test_bag_of_words():
    assert list(bag_of_words(ex_tokenized_text_one, ex_all_words)) == [0.0, 1.0,
                                                                       1.0, 0.0,
                                                                       1.0, 0.0,
                                                                       0.0, 1.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0]

    assert list(bag_of_words(ex_tokenized_text_two, ex_all_words)) == [0.0, 1.0,
                                                                       1.0, 1.0,
                                                                       1.0, 0.0,
                                                                       0.0, 1.0,
                                                                       0.0, 0.0,
                                                                       0.0, 1.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 0.0,
                                                                       0.0, 1.0,
                                                                       1.0, 1.0]

#Tests for the NeuralNet class:
#Each of the functions below is necessary to check that the method in the NeuralNet class is working correctly
@pytest.fixture
def test_odessa_model():
    input_size = 10
    hidden_size = 8
    num_classes = 3
    return NeuralNet(input_size, hidden_size, num_classes)

@pytest.fixture
def data_input():
    batch_size = 8
    input_size = 10
    return torch.randn(batch_size, input_size)

#Trying to verify that we have the correct shape or dimensions for the model using an actual and expected shapes
def test_forward_dimensions(test_odessa_model, data_input):
    output = test_odessa_model(data_input)
    assert output.shape == (data_input.shape[0], test_odessa_model.layer3.out_features), "The dimensions of the output are wrong."

#Trying to verify that the model's output does not include any values that are not numbers (NaN)
def test_forward_no_nan(test_odessa_model, data_input):
    output = test_odessa_model(data_input)
    assert not torch.isnan(output).any(), "This output contains values that are not numbers (NaN)."



ex_message_one = "What is a headache?"
ex_message_two = "What is a concussion?"
ex_message_three = "How do you prevent a headache?"
ex_message_fail = "I have a dog."
ex_message_four = "I would like to talk about a potential injury."
ex_message_five = "Could you define a headache?"

#Tests for the function get_message
#This function only tests cases where the responses included will receive the same response, regardless of
#how distinct they are
def test_get_message():
    assert get_message(ex_message_fail) == "I do not understand. Could you please clarify?"
    assert get_message(ex_message_one) == "A headache is a condition where an individual will experience pain in the head or face that can feel constant, sharp, dull, or even like placing pressure on one’s head."
    assert get_message(ex_message_two) == "A concussion is a brain injury that transpires when force is transmitted to the brain, which results in the brain moving fast within the skull. People commonly receive concussions with a direct blow to the head that causes the brain to rock violently within the skull."
    assert get_message(ex_message_three) == "To prevent headaches, people can avoid triggers such as lack of sleep, change eating habits, exercise, rest in a quiet, dark location, medicine, and stress management. Please see a doctor immediately if the pain is persistent and extremely uncomfortable."
    assert get_message(ex_message_five) == "A headache is a condition where an individual will experience pain in the head or face that can feel constant, sharp, dull, or even like placing pressure on one’s head."


def test_get_message_with_mock():
    ex_bot = OdessaApplication()
    question = "I would like to talk about a potential injury."
    expected_response = "I am open to hearing about any issues that you would like to discuss."

    with patch("random.choice"), return_value=expected_response):
        response = ex_bot.get_response(question)
        assert response == expected_response


