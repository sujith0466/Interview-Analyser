# utils/nlp_analysis.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text using VADER.
    
    Returns:
        sentiment_label (str): 'Positive', 'Negative', or 'Neutral'
        scores (dict): Dictionary with 'neg', 'neu', 'pos', and 'compound' scores
    """
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = 'Positive'
    elif compound <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, scores
