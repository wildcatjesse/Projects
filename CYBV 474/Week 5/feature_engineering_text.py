# setup
#from mlwpy import *
import textwrap
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline


#import cv2
docs = ["the cat in the hat",
        "the cow jumped over the moon",
        "the cat mooed and the cow meowed",
        "the cat said to the cow cow you are not a cat"]

vocabulary = set(" ".join(docs).split())

common_words = set(['a', 'to', 'the', 'in', 'and', 'are'])
vocabulary = vocabulary - common_words
print(textwrap.fill(str(vocabulary)))
doc_contains = [{w:(w in d) for w in vocabulary} for d in docs]
print(doc_contains)