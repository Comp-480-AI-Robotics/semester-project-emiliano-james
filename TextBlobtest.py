from textblob import TextBlob
import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# Need to install brown, punkt, wordnet, averaged_perceptron_tagger, conll2000, movie_reviews
# nltk.download()

input = input("Talk to me! ")
wiki = TextBlob(input)
print("Polarity:", wiki.sentiment.polarity, "Subjectivity:", wiki.sentiment.subjectivity)