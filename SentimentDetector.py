from textblob import TextBlob
import nltk
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# # Need to install brown, punkt, wordnet, averaged_perceptron_tagger, conll2000, movie_reviews
# nltk.download()

class SentimentDetector:

    def getSentiment(self, sentence):
        txt = TextBlob(sentence)
        emotion = ""
        polarity = txt.sentiment.polarity

        if -0.2 <= polarity <= 0.2:
            emotion = "Neutral"
        elif 0.2 < polarity <= 0.6:
            emotion = "Somewhat positive"
        elif 0.6 < polarity <= 1.0:
            emotion = "Very positive"
        elif -0.6 <= polarity < -0.2:
            emotion = "Somewhat negative"
        elif -1 <= polarity < -0.6:
            emotion = "Very negative"

        return emotion

