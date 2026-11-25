from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r"[a-z0-9]+")
stemmer = PorterStemmer()


def preprocess(text):
    text = text.lower()
    words = tokenizer.tokenize(text)
    words = [w for w in words if w not in stop_words]
    words = [stemmer.stem(w) for w in words]
    return " ".join(words)


