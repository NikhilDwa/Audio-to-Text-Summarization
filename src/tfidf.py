import math


def tf_evaluation(word_frequency_in_sentence: dict) -> dict:
    """
        Return a dictionary with values is dictionary evaluating count of word in document divided by number of words in document

        Inputs: dictionary with values in dictionary as well

        Returns:
        - dictionary with values is dictionary.
    """

    tf_result = {}
    for sentence, word_frequency in word_frequency_in_sentence.items():
        tf_table = {}
        sentence_length = len(word_frequency)
        for word in word_frequency.keys():
            tf_table[word] = round(word_frequency[word] / sentence_length, 2)
        tf_result[sentence] = tf_table

    return tf_result


def idf_evaluation(word_frequency_in_sentence: dict, word_sentence_frequency: dict) -> dict:
    """
        Return a dictionary with word as keys and result of idf evaluation of each word as values.

        Inputs: two dictionary; one with sentence in keys and number of words values with key-value pair as word and count.
            second with key-value pair as word and count.

        Returns:
        - dictionary with values is dictionary.
    """

    total_sentences = len(word_frequency_in_sentence.keys())
    idf_result = {}
    for sentence, word_frequency in word_frequency_in_sentence.items():
        idf_table = {}
        for word in word_frequency.keys():
            idf_table[word] = round(math.log(total_sentences / word_sentence_frequency[word] + 1), 2)
        idf_result[sentence] = idf_table

    return idf_result


def tf_idf_evaluation(tf: dict, idf: dict) -> dict:
    """
        Return a dictionary with values multiplying corresponding tf and idf.

        Inputs: tf as dictionary and idf as dictionary.

        Returns:
        - dictionary with values multiplying corresponding tf and idf.
    """

    tf_idf_result = {}
    for (tf_sentence, tf_table), (idf_sentence, idf_table) in zip(tf.items(), idf.items()):
        tfidf_table = {}
        for (tf_word, tf_value), (idf_word, idf_value) in zip(tf_table.items(), idf_table.items()):
            tfidf_table[tf_word] = round(tf_value * idf_value, 2)
        tf_idf_result[tf_sentence] = tfidf_table

    return tf_idf_result
