import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLTK is a powerful Python library for natural language processing."
words = word_tokenize(text)
sentences = sent_tokenize(text)

print(words)
print(sentences)

['NLTK', 'is', 'a', 'powerful', 'Python', 'library', 'for', 'natural', 'language', 'processing', '.']
['NLTK is a powerful Python library for natural language processing.']
