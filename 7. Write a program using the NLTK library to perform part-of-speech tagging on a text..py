import nltk
from nltk.tokenize import word_tokenize
text = "I love eating pizza with cheese and drinking soda."
tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
print("Part-of-Speech Tagging:")
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")
