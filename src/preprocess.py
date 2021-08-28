import re


class CleanText:
    def __init__(self, text):
        self.text = text

    def clean_sentences(self: str) -> str:
        """
            Return a string with sentences starting with only with alphabets and string
            with no extra white-spaces between the words.

            Inputs: text in string

            Returns:
            - clean text in string.
        """

        split_sentence = self.text.split(". ")
        cleaned_text = []
        for sentence in split_sentence:
            sentence = re.sub(r"[^a-zA-Z]", " ", sentence)  # return white-space if the first character of sentence is not alphabetic
            sentence = re.sub(r"\s+", " ", sentence)  # return white-space if any white-space character, one or more times
            cleaned_text.append(sentence)
        cleaned_text = '. '.join(cleaned_text)

        return cleaned_text
