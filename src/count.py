import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize, PorterStemmer

stopwords = set(stopwords.words('english'))
ps = PorterStemmer()


def frequency_of_words(text: str) -> dict:
    """
        Return a dictionary, calculate each word frequency present in the input text.

        Inputs: text in string

        Returns:
        - word frequency in dictionary.
    """

    words = word_tokenize(text)
    word_frequency = dict()
    for word in words:
        word = ps.stem(word.lower())
        if (word not in stopwords) and (len(word) > 2):
            if word not in word_frequency.keys():
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1

    return word_frequency


def each_word_frequency_in_sentence(text: str) -> dict:
    """
        Return a dictionary, calculate each word frequency present in each sentences.

        Inputs: text in string

        Returns:
        - the starting of sentences and its word frequency in dictionary.
    """

    each_word_frequency = dict()
    for sentence in sent_tokenize(text):
        each_word_frequency[sentence] = frequency_of_words(sentence)

    return each_word_frequency


def sentence_frequency_of_each_word(each_word_frequency: dict) -> dict:
    """
        Return a dictionary, calculating how many sentences contain the particular word in the text.

        Inputs: the starting of sentences and its word frequency in dictionary.

        Returns:
        - a dictionary with how many sentences contain the particular word in the text.
    """

    sentence_count = {}
    for sentence, frequency_dictionary in each_word_frequency.items():
        for word in frequency_dictionary.keys():
            if word not in sentence_count.keys():
                sentence_count[word] = 1
            else:
                sentence_count[word] = sentence_count[word] + 1

    return sentence_count
