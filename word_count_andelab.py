from collections import Counter
def word_count(sentence):
    words = sentence.split(' ')
    wordoccurence = Counter(words)
