from nltk import sent_tokenize


def tf_idf_score(tf_idf: dict) -> dict:
    """
        Return a dictionary with sentences as keys and sum of tfidf of each words as values.

        Inputs: dictionary with sentences and tfidf evaluation of each word of the sentences

        Returns:
        - dictionary with sum of tfidf of each words as values.
    """

    sentence_score = {}
    for sentence, tfidf_value in tf_idf.items():
        for word, value in tfidf_value.items():
            if sentence not in sentence_score.keys():
                sentence_score[sentence] = value
            else:
                sentence_score[sentence] += value

    return sentence_score


def average_score(sentence_score: dict) -> float:
    """
        Return average score as float, totaling all the score divided by the number of sentences.

        Inputs: dictionary with sentences and their corresponding tfidf score.

        Returns:
        - sum of all the score divided by the number of sentences.
    """

    sum_sentence = 0
    for value in sentence_score.values():
        sum_sentence += value
    avg_score = round(sum_sentence/len(sentence_score), 2)

    return avg_score


def text_summary(text: str, tfidf_sentence_score: dict, threshold: float) -> str:
    """
        Return the summary of the input text according to threshold value.

        Inputs: input text as first argument, all the sentences tfidf score as second argument and the threshold.

        Returns:
        - summary of the text in string.
    """

    sentences = sent_tokenize(text)
    summary = ""
    for sentence in sentences:
        if (sentence in tfidf_sentence_score) and tfidf_sentence_score[sentence] >= threshold:
            summary += " " + sentence

    return summary
