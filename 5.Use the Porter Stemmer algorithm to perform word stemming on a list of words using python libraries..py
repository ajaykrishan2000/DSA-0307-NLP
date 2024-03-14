import nltk
from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
words = ["running", "runner", "ran", "easily", "fairly", "fairness"]
stemmed_words = [porter_stemmer.stem(word) for word in words]
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} => {stemmed}")
