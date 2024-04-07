from nltk import ne_chunk

text = "Barack Obama was born in Hawaii."
words = word_tokenize(text)
tags = pos_tag(words)
ner_tags = ne_chunk(tags)

print(ner_tags)

(S
  (PERSON Barack/NNP)
  (PERSON Obama/NNP)
  was/VBD
  born/VBN
  in/IN
  (GPE Hawaii/NNP)
  ./.)
