from nltk import pos_tag

words = word_tokenize("NLTK is a powerful Python library for NLP.")
tags = pos_tag(words)

print(tags)


[('NLTK', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('powerful', 'JJ'), ('Python', 'NNP'), ('library', 'NN'), ('for', 'IN'), ('NLP', 'NNP'), ('.', '.')]
