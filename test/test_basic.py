import sys
# sys.path.insert(0, r'F:\Leapfrog Technology\Major Project')
import pytest

from src import CleanText
from src import tf_idf_score, average_score, text_summary
from src import tf_evaluation, idf_evaluation, tf_idf_evaluation
from src import frequency_of_words, each_word_frequency_in_sentence, sentence_frequency_of_each_word


# Testing of CleanText class
def test_clean_sentences():
    output_1 = CleanText("Programming is  fun.")
    output_2 = CleanText("123 Programming is  fun.")
    assert type(output_1.clean_sentences()) != int
    assert type(output_1.clean_sentences()) == str
    assert output_1.clean_sentences() == "Programming is fun."
    assert output_2.clean_sentences() == " Programming is fun."
    assert output_2.clean_sentences() != "Programming is fun"


# Testing of frequency_of_words function
def test_count_words():
    output = frequency_of_words('Programming is fun.')
    assert type(output) == dict
    assert output == {'fun': 1, 'program': 1}
    assert output != {'fun': 1, 'Program': 1}
    assert output != {'fun': 1, 'programming': 1}


# Testing of each_word_frequency_in_sentence function
def test_count_words_in_sentence():
    text = 'We love to do coding.'
    output = each_word_frequency_in_sentence(text)
    assert type(output) == dict
    assert output == {'We love to do coding.': {'love': 1, 'code': 1}}


# Testing of sentence_frequency_of_each_word function
def test_sentence_frequency_of_each_word():
    text = {'We love to do coding': {'love': 1, 'code': 1}}
    output = sentence_frequency_of_each_word(text)
    assert type(output) == dict
    assert output == {'love': 1, 'code': 1}
    assert output != {'we': 1, 'love': 1, 'to': 1, 'do': 1, 'code': 1}


# Testing of tf_evaluation function
def test_tf():
    dict_example = {'We love to do coding in python.': {'love': 1, 'code': 1, 'python': 1}}
    dict_example_1 = {'We love to do coding in python.': {'love': 2, 'code': 1, 'python': 1}}
    output_1 = tf_evaluation(dict_example)
    output_2 = tf_evaluation(dict_example_1)
    assert type(output_1) == dict
    assert output_1 == {'We love to do coding in python.': {'code': 0.33, 'love': 0.33, 'python': 0.33}}
    assert output_2 == {'We love to do coding in python.': {'code': 0.33, 'love': 0.67, 'python': 0.33}}
    assert output_2 != {'We love to do coding in python.': {'code': 0.25, 'love': 0.50, 'python': 0.25}}


# Testing of idf_evaluation function
def test_idf():
    dict_1 = {'We love to do coding in python.': {'love': 1, 'code': 1, 'python': 1}}
    dict_2 = {'love': 2, 'code': 1, 'python': 1}
    output = idf_evaluation(dict_1, dict_2)
    assert type(output) == dict
    assert type(output) != str
    assert output == {'We love to do coding in python.': {'code': 0.69, 'love': 0.41, 'python': 0.69}}
    assert output != {'We love to do coding in python.': {'code': 0, 'love': 0.39, 'python': 0}}


# Testing of tf_idf_evaluation function
def test_tfidf():
    tf = {'We love to do coding in python.': {'love': 0.33, 'code': 0.33, 'python': 0.33}}
    idf = {'We love to do coding in python.': {'love': 0.41, 'code': 0.69, 'python': 0.69}}
    output = tf_idf_evaluation(tf, idf)
    assert type(output) == dict
    assert output == {'We love to do coding in python.': {'code': 0.23, 'love': 0.14, 'python': 0.23}}


# Testing of tf_idf_score function
def test_tf_idf_score():
    dict_example = {'We love to do coding in python.': {'code': 0.23, 'love': 0.14, 'python': 0.23}}
    output = tf_idf_score(dict_example)
    assert type(output) == dict
    assert output == {'We love to do coding in python.': 0.6}


# Testing of average_score function
def test_average_score():
    dict_example = {'We love to do coding in python.': 0.6}
    output = average_score(dict_example)
    assert type(output) == float
    assert type(output) != str
    assert output == 0.6


# Testing of text_summary function
def test_summary():
    text = 'We love to do coding in python.'
    dict_example = {'We love to do coding in python.': 0.6}
    output = text_summary(text, dict_example, 0.6)
    assert type(output) == str
    assert output == ' We love to do coding in python.'
    assert output != ' We love to do coding in python'
