'''
WK 6
Demonstration
Professor Hand
Spring 2023
'''
# import python standard libraries
from collections import Counter
import re

#import python 3rd party libs
from nltk import word_tokenize, pos_tag, FreqDist, trigrams, bigrams
from prettytable import PrettyTable

# PSUEDO CONTANTS
'''
Assumes that the debateRaw.txt file is in the 
same folder as the script
'''
DEBATE_FILE = "debateRaw.txt"    

def main():
    
    bidenText = ''  # emtpy string to hold Biden responses
    print("Processing Biden Results Only")
    with open(DEBATE_FILE) as debate:
        for eachLine in debate:
            eachLine = eachLine.lower()
            # Process Eachline where Biden is speaking
            if "joe biden" in eachLine[:10]:
                bidenText = bidenText + eachLine[10:]
    
    # Remove any punctation or other characters from the speach
    bidenText = re.sub("[^a-zA-Z ]", ' ', bidenText)
    
    # Tokenize the speech
    words = word_tokenize(bidenText)
    triGrams = list(trigrams(words))
    biGrams  = list(bigrams(words))

    print("Joe Biden - Bigrams and Trigrams Results\n")
    print("\nBigrams")
    for eachBigram in biGrams:
        print(eachBigram)
    
    print("\nTrigrams")
    for eachTrigram in triGrams:
        print(eachTrigram)    

    # Apply part of speech tags to each word
    tags = pos_tag(words)
    for eachWord in tags:
        print(eachWord)    
    # Obtain counts for each tag
    counts = Counter( tag for word,  tag in tags)
    
    fd = FreqDist(counts)
    tbl = PrettyTable(['TAG', 'COUNT'])
    for tag, count in fd.items():
        tbl.add_row([tag, count])
    
    print(tbl.get_string(sortby='COUNT', reversesort=True))
    
    ''' Plot Biden Tagged Part of Speech Tagging '''
    fd.plot()
 
# Main Program Starts Here
#===================================

if __name__ == '__main__':
    main()


            