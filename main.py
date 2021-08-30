import os

import streamlit as st

from src import CleanText
from src import AudioText
from src import tf_idf_score, average_score, text_summary
from src import tf_evaluation, idf_evaluation, tf_idf_evaluation
from src import each_word_frequency_in_sentence, sentence_frequency_of_each_word


def audio_to_text(path: str) -> str:
    """
        Return text converted from the input audio using google recognizer.

        Inputs: path of the audio file

        Returns:
        - text in string.
    """

    audio_note = AudioText(path)
    audio_text = audio_note.speech_text()

    return audio_text


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


def main():
    st.title("Audio to Text Summarization")
    st.subheader("Upload audio file in wav format")
    audio_file = st.file_uploader("File", type=['wav'])
    path = ''

    if audio_file is not None:
        st.audio(audio_file)
        with open(os.path.join("Media", audio_file.name), "wb") as f:
            f.write(audio_file.getbuffer())
        path = 'Media' + '/' + audio_file.name

        text_of_audio = audio_to_text(path)

        text = text_of_audio
        st.subheader("Text from audio")
        st.success('{}'.format(text))

        result = text_summarization(text)
        st.subheader("Text Summary")
        st.success('{}'.format(result))


if __name__ == '__main__':
    main()
