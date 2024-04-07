from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
text = "NLTK is awesome!"
sentiment_score = sia.polarity_scores(text)

print(sentiment_score)

{'neg': 0.0, 'neu': 0.313, 'pos': 0.687, 'compound': 0.6588}
