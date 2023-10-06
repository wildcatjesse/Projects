'''
CYBV-474 POS PLOT EXAMPLE
FEB 22
'''
from nltk import word_tokenize, pos_tag, FreqDist
from collections import Counter
import re
sampleText = 'thank you. We have to take a quick break. When we come back, the Democratic Presidential Debate continues right after this. Only on CBS'

'''  Strip any punctuation '''
sampleText = re.sub("[^a-zA-Z ]", ' ', sampleText)

words = word_tokenize(sampleText) # Tokenize text
tags = pos_tag(words) # Part of Speech Tagging

''' tally each category'''
counts = Counter( tag for word,  tag in tags)

fd = FreqDist(counts)  # Calculate the distribution
fd.plot(title="Part of Speech Tagging Example")
