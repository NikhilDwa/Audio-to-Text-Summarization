import os
import ntpath

import nltk
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence

r = sr.Recognizer()


class AudioText:
    def __init__(self, path: str):
        self.path = path

    def speech_text(self) -> str:
        """
            Return text converted from the input audio using google recognizer.

            Inputs: path of the audio file

            Returns:
            - text in string.
        """

        sound = AudioSegment.from_wav(self.path)
        chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS-14, keep_silence=500,)
        head, tail = ntpath.split(self.path)
        to_be_folder = os.path.splitext(tail)[0]
        folder_name = "Media/" + to_be_folder + "-chunks"
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        text_from_audio = ""
        for i, audio_chunk in enumerate(chunks, start=1):
            chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
            audio_chunk.export(chunk_filename, format="wav")
            with sr.AudioFile(chunk_filename) as source:
                audio_note = r.record(source)
                try:
                    text = r.recognize_google(audio_note)
                except sr.UnknownValueError as e:
                    print("Error:", str(e))
                else:
                    text = f"{text.capitalize()}. "
                    text_from_audio = text_from_audio + text

        return text_from_audio
