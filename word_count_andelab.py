from collections import Counter
def word_count(sentence):
    words = sentence.split(' ')
    wordoccurence = Counter(words)
    for k,v in wordoccurence.items():
        print('{0}: {1}'.format(k,v))
        
