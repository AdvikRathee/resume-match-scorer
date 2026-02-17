import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return text.lower()


def preprocess(text):
    """
    Clean, tokenize, remove stopwords, and lemmatize text.
    """

    text = clean_text(text)
    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and len(token) > 2
    ]

    return " ".join(tokens)
