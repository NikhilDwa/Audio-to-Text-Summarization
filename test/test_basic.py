import sys
# sys.path.insert(0, r'F:\Leapfrog Technology\Major Project')
import pytest

from src import CleanText
from src import tf_idf_score, average_score, text_summary
from src import tf_evaluation, idf_evaluation, tf_idf_evaluation
from src import frequency_of_words, each_word_frequency_in_sentence, sentence_frequency_of_each_word


# Type testing of CleanText
def test_clean_sentences_1():
    output = CleanText("123 Programming is  fun.")
    assert type(output.clean_sentences()) == str


# Testing Preprocessing of the input text
def test_clean_sentences_2():
    output_1 = CleanText("Programming is  fun.")
    output_2 = CleanText("123 Programming is  fun.")
    assert output_1.clean_sentences() == "Programming is fun." and output_2.clean_sentences() == " Programming is fun."


# Type testing of frequency_of_words
def test_count_1():
    output = frequency_of_words('Programming is fun.')
    assert type(output) == dict


def test_count_2():
    output = frequency_of_words('Programming is fun.')
    assert output == {'fun': 1, 'program': 1}


# Type testing of each_word_frequency_in_sentence
def test_count_3():
    text = 'We love to do coding.'
    output = each_word_frequency_in_sentence(text)
    assert type(output) == dict


# count of word in each sentences
def test_count_4():
    text = 'We love to do coding.'
    output = each_word_frequency_in_sentence(text)
    assert output == {'We love to do coding.': {'love': 1, 'code': 1}}


# Type testing of sentence_frequency_of_each_word function
def test_count_5():
    text = {'We love to do coding': {'love': 1, 'code': 1}}
    output = sentence_frequency_of_each_word(text)
    assert type(output) == dict


# count of sentences in the document with particular word
def test_count_6():
    output = sentence_frequency_of_each_word({'We love to do coding': {'love': 1, 'code': 1}})
    assert output == {'love': 1, 'code': 1}


# Type testing of tf_evaluation function
def test_tfidf_1():
    dict_example = {'We love to do coding in python.': {'love': 1, 'code': 1, 'python': 1}}
    output = tf_evaluation(dict_example)
    assert type(output) == dict


# TF evaluation testing
def test_tfidf_2():
    dict_example = {'We love to do coding in python.': {'love': 1, 'code': 1, 'python': 1}}
    output = tf_evaluation(dict_example)
    assert output == {'We love to do coding in python.': {'code': 0.33, 'love': 0.33, 'python': 0.33}}


def test_tfidf_3():
    dict_example = {'We love to do coding in python.': {'love': 2, 'code': 1, 'python': 1}}
    output = tf_evaluation(dict_example)
    assert output == {'We love to do coding in python.': {'code': 0.33, 'love': 0.67, 'python': 0.33}}


# Type testing of idf_evaluation function
def test_tfidf_4():
    dict_1 = {'We love to do coding in python.': {'love': 1, 'code': 1, 'python': 1}}
    dict_2 = {'love': 2, 'code': 1, 'python': 1}
    output = idf_evaluation(dict_1, dict_2)
    assert type(output) == dict and type(output) != str


# IDF evaluation testing
def test_tfidf_5():
    dict_1 = {'We love to do coding in python.': {'love': 1, 'code': 1, 'python': 1}}
    dict_2 = {'love': 2, 'code': 1, 'python': 1}
    output = idf_evaluation(dict_1, dict_2)
    assert output == {'We love to do coding in python.': {'code': 0.69, 'love': 0.41, 'python': 0.69}}


# Type testing of tf_idf_evaluation function
def test_tfidf_6():
    tf = {'We love to do coding in python.': {'love': 0.33, 'code': 0.33, 'python': 0.33}}
    idf = {'We love to do coding in python.': {'love': 0.41, 'code': 0.69, 'python': 0.69}}
    output = tf_idf_evaluation(tf, idf)
    assert type(output) == dict


# TF_IDF evaluation
def test_tfidf_7():
    tf = {'We love to do coding in python.': {'love': 0.33, 'code': 0.33, 'python': 0.33}}
    idf = {'We love to do coding in python.': {'love': 0.41, 'code': 0.69, 'python': 0.69}}
    output = tf_idf_evaluation(tf, idf)
    assert output == {'We love to do coding in python.': {'code': 0.23, 'love': 0.14, 'python': 0.23}}


# Type testing of tf_idf_score function
def test_summary_1():
    dict_example = {'We love to do coding in python.': {'code': 0.23, 'love': 0.14, 'python': 0.23}}
    output = tf_idf_score(dict_example)
    assert type(output) == dict


# TF-IDF score testing
def test_summary_2():
    dict_example = {'We love to do coding in python.': {'code': 0.23, 'love': 0.14, 'python': 0.23}}
    output = tf_idf_score(dict_example)
    assert output == {'We love to do coding in python.': 0.6}


# Type testing of average_score function
def test_summary_3():
    dict_example = {'We love to do coding in python.': 0.6}
    output = average_score(dict_example)
    assert type(output) == float


# Average score testing
def test_summary_4():
    dict_example = {'We love to do coding in python.': 0.6}
    output = average_score(dict_example)
    assert output == 0.6


# Type testing of text_summary function
def test_summary_5():
    text = 'We love to do coding in python.'
    dict_example = {'We love to do coding in python.': 0.6}
    output = text_summary(text, dict_example, 0.6)
    assert type(output) == str


# Summary of the input text
def test_summary_6():
    text = 'We love to do coding in python.'
    dict_example = {'We love to do coding in python.': 0.6}
    output = text_summary(text, dict_example, 0.6)
    assert output == ' We love to do coding in python.'
