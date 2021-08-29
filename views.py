import os
import streamlit as st

from src import speech_text
from main import text_summarization


st.title("Audio to Text Summarization")
st.subheader("Upload audio file in wav format")
audio_file = st.file_uploader("File", type=['wav'])
path = ''

if audio_file is not None:
    st.audio(audio_file)
    with open(os.path.join("Media", audio_file.name), "wb") as f:
        f.write(audio_file.getbuffer())
    path = 'Media' + '/' + audio_file.name

    text_of_audio = speech_text(path)

    text = text_of_audio
    st.subheader("Text from audio")
    st.success('{}'.format(text))

    result = text_summarization(text)
    st.subheader("Text Summary")
    st.success('{}'.format(result))
