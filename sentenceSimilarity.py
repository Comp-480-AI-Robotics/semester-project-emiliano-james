from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn

# https://nlpforhackers.io/wordnet-sentence-similarity/

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None

def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None


def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    score, count = 0.0, 0

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        simlist = [synset.path_similarity(ss) for ss in synsets2 if synset.path_similarity(ss) is not None]
        if not simlist:
            continue;
        best_score = max(simlist)

        # Check that the similarity could have been computed
        score += best_score
        count += 1

    if count == 0:
        return 0

    # Average the values
    score /= count
    return score


sentences = [
    "I am happy.",
    "I am sad.",
    "I am angry.",
    "I am scared.",
    "I am disgusted.",
    "I am surprised."
]

focus_sentence = "Today is a good day."

for sentence in sentences:
    print("Similarity(\"%s\", \"%s\") = %s" % (focus_sentence, sentence, sentence_similarity(focus_sentence, sentence)))
    print("Similarity(\"%s\", \"%s\") = %s" % (sentence, focus_sentence, sentence_similarity(sentence, focus_sentence)))
    print("")

    # Similarity("Cats are beautiful animals.", "Dogs are awesome.") = 0.511111111111
    # Similarity("Dogs are awesome.", "Cats are beautiful animals.") = 0.666666666667

    # Similarity("Cats are beautiful animals.", "Some gorgeous creatures are felines.") = 0.833333333333
    # Similarity("Some gorgeous creatures are felines.", "Cats are beautiful animals.") = 0.833333333333

    # Similarity("Cats are beautiful animals.", "Dolphins are swimming mammals.") = 0.483333333333
    # Similarity("Dolphins are swimming mammals.", "Cats are beautiful animals.") = 0.4

    # Similarity("Cats are beautiful animals.", "Cats are beautiful animals.") = 1.0
    # Similarity("Cats are beautiful animals.", "Cats are beautiful animals.") = 1.0