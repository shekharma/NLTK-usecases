from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

word = "running"
stemmed_word = stemmer.stem(word)
lemmatized_word = lemmatizer.lemmatize(word)

print("Stemmed Word:", stemmed_word)
print("Lemmatized Word:", lemmatized_word)

Stemmed Word: run
Lemmatized Word: running
