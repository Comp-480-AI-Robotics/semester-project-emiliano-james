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

while True:
    txt = input("Talk to me! (Type 'q' to quit) ")
    wiki = TextBlob(txt)

    if wiki.lower() == "q":
        break

    emotion = ""
    polarity = wiki.sentiment.polarity
    subjectivity = wiki.sentiment.subjectivity

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

    print("Polarity:", polarity, "Subjectivity:", subjectivity, "Emotion:", emotion, "\n")