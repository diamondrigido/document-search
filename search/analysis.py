import re
import string

import pymorphy2
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer


STOPWORDS_RU = stopwords.words("russian")
STOPWORDS_EN = stopwords.words("english")
PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))


def tokenize(text):
    return text.split()

def lowercase_filter(tokens):
    return [token.lower() for token in tokens]

def punctuation_filter(tokens):
    return [PUNCTUATION.sub('', token) for token in tokens]

def stopword_filter_ru(tokens):
    return [token for token in tokens if token not in STOPWORDS_RU]

def stopword_filter_en(tokens):
    return [token for token in tokens if token not in STOPWORDS_EN]

def stem_filter_ru(tokens):
    morph = pymorphy2.MorphAnalyzer()
    lst = []
    for token in tokens:
        lst.append(morph.parse(token)[0].normal_form)
    return lst

def stem_filter_en(tokens):
    snowball = SnowballStemmer(language="english")
    lst = []
    for token in tokens:
        lst.append(snowball.stem(token))
    return lst

def analyze_ru(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter_ru(tokens)
    tokens = stem_filter_ru(tokens)

    return [token for token in tokens if token]

def analyze_en(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter_en(tokens)
    tokens = stem_filter_en(tokens)

    return [token for token in tokens if token]