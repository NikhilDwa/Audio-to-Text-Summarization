import nltk
import numpy as np

from src import CleanText
from src import tf_idf_score, average_score, text_summary
from src import tf_evaluation, idf_evaluation, tf_idf_evaluation
from src import each_word_frequency_in_sentence, sentence_frequency_of_each_word


def text_summarization(text: str) -> str:
    """
        Return a summary of the text converted from the audio.

        Inputs: text converted from audio in string

        Returns:
        - summary text in string.
    """

    text_to_summarize = CleanText(text)
    preprocessed_text = text_to_summarize.clean_sentences()
    each_word_frequency = each_word_frequency_in_sentence(preprocessed_text)
    word_sentence_frequency = sentence_frequency_of_each_word(each_word_frequency)

    #  TF-IDF calculation of the input text
    tf = tf_evaluation(each_word_frequency)
    idf = idf_evaluation(each_word_frequency, word_sentence_frequency)
    tfidf = tf_idf_evaluation(tf, idf)

    #  Scores of the document
    tfidf_score = tf_idf_score(tfidf)
    avg_score = average_score(tfidf_score)

    #  Summary of the input text
    summary = text_summary(text, tfidf_score, avg_score)

    return summary


if __name__ == "__main__":
    main()
