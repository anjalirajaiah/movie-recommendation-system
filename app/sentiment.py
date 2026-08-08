from nltk.sentiment import SentimentIntensityAnalyzer

# Create analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    return score['compound']
