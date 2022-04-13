"""  =================================================================
File: SentimentDetector.py
This file contains code for the SentimentDetector class that can detect
sentiment from text input using TextBlob.
Authors: Anh Nguyen, Lily Irvin, Ryan Specht
Contributors: Emiliano Huerta, James Yang
 ==================================================================="""
from textblob import TextBlob


class SentimentDetector:
    """Represents a sentiment detector object"""

    def getSentiment(self, sentence):
        """Detects the sentiment of a sentence using TextBlob"""
        txt = TextBlob(sentence)
        sentiment = ""
        polarity = txt.sentiment.polarity

        # The 5 sentiments available are very positive, somewhat positive,
        # neutral, somewhat negative, and very negative
        if -0.2 <= polarity <= 0.2:
            sentiment = "neutral"
        elif 0.2 < polarity <= 0.6:
            sentiment = "somewhat positive"
        elif 0.6 < polarity <= 1.0:
            sentiment = "very positive"
        elif -0.6 <= polarity < -0.2:
            sentiment = "somewhat negative"
        elif -1 <= polarity < -0.6:
            sentiment = "very negative"
        print("this is the polarity of responses", polarity)
        return sentiment
