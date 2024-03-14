import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
def morphological_analysis(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for token in tokens:
        lemmatized_word = lemmatizer.lemmatize(token)
        lemmatized_words.append(lemmatized_word)
    return tokens, lemmatized_words
def main():
    text = "The cats are chasing mice and birds in the garden."
    original_words, lemmatized_words = morphological_analysis(text)
    print("Original Words:", original_words)
    print("Lemmatized Words:", lemmatized_words)

if __name__ == "__main__":
    main()
