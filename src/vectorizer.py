from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_vectorize(texts):
    """
    Convert list of texts into TF-IDF vectors
    """
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors
