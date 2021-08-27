import re


def clean_sentences(text):
    split_sentence = text.split(". ")
    cleaned_text = []
    for sentence in split_sentence:
        sentence = re.sub(r"[^a-zA-Z]", " ", sentence)
        sentence = re.sub(r"\s+", " ", sentence)
        cleaned_text.append(sentence)
    cleaned_text = '. '.join(cleaned_text)
    return cleaned_text
