import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

def extract_keywords(text, top_n=5):
    """
    Extract keywords from a sentence/text by removing stopwords.

    Args:
        text (str): Input text.
        top_n (int): Number of top keywords to return.

    Returns:
        List[str]: List of keywords.
    """
    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalpha() and w not in STOPWORDS]
    freq = nltk.FreqDist(words)
    return [word for word, _ in freq.most_common(top_n)]

def summarize_text(text, num_sentences=1):
    """
    Return the first few sentences as a simple summary.

    Args:
        text (str): Input text.
        num_sentences (int): Number of sentences to return.

    Returns:
        str: Summary text.
    """
    sentences = sent_tokenize(text)
    return " ".join(sentences[:num_sentences])
