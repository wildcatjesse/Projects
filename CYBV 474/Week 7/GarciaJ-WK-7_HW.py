# Script Module Importing


# Python Standard Library Modules
import os           # Operating/Filesystem Module
import time         # Basic Time Module


# Import 3rd Party Modules
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
from nltk import word_tokenize, pos_tag, FreqDist
import collections

# End of Script Module Importing


# Psuedo Constants
SCRIPT_NAME    = "Script: Week 7 Assignment"
SCRIPT_VERSION = "Version 3.0"
SCRIPT_AUTHOR  = "Author: Jesus Garcia"

DEBATE_FILE = "speechByCandidate.csv"
# End of Script Constants

stops = set(stopwords.words('english'))

topWords = {}

# Script Functions
def GetTime(timeStyle="UTC"):
    '''
    Function: GetTime()
    Input timeStyle either UTC or LOCAL
          UTC is the default if not argument is provided
    Returns a string containing the current time

    Description:
    Script will use the local system clock, time, date and timezone
    to calcuate the current time.  Thus you should sync your system
    clock before using this script

    '''
    epochValue = time.time()

    if timeStyle == 'UTC':
        utcTime = time.gmtime(epochValue)
        timeString = time.asctime(utcTime)
        return 'UTC Time: ' + timeString
    elif timeStyle == 'LOCAL':
        localTime = time.localtime(epochValue)
        timeString = time.asctime(localTime)
        return 'Local Time: ' + timeString
    else:
        return "Invalid TimeStyle Specified"
# End GetTime Function

def CountElement(elem):
    return elem[1]

# this will be a dictionary of caidates and word counts
candidates = {}
def main():
    with open(DEBATE_FILE) as debate:
        for eachLine in debate:

            eachLine = eachLine.lower()
            lineList = eachLine.split(',')
            wordList = lineList[1].split()
            counts = Counter(wordList)
            # line will create dict of the candidate and freq dist counts as a dictionary.
            # using this way to create a dataframe easier.
            candidates[lineList[0]] = dict(FreqDist(counts).items())

            for eachWord in wordList:

                if eachWord not in stops and len(eachWord) >= 5:
                    try:
                        cnt = topWords[eachWord]
                        cnt += 1
                        topWords[eachWord] = cnt
                    except:
                        topWords[eachWord] = 1

        topWordList = list(topWords.items())
        topWordList.sort(key=CountElement, reverse=True)
        # assigning the keys of above list of tuples for for columns of our dataframe
    cols = [t[0] for t in topWordList[:50]]


    # loop to store only the top words from my cols variable for each candidate
    for i,j in candidates.items():
        temp_dict = {}
        for word in cols:
            try:
                temp_dict[word] = j[word]
            except  KeyError:
                temp_dict[word] = 0
        candidates[i] = temp_dict

    temp_df = pd.DataFrame.from_dict(candidates, orient='index')
    pd.set_option('display.max_columns',None)
    #print(temp_df)
    temp_df.to_csv('GarciaJ_WK-7_Output.csv')



# End of Script Functions


# Script Classes

# End of Script Classes


# Main Script Starts Here

if __name__ == '__main__':
    # Print Basic Script Information

    print()
    print(SCRIPT_NAME)
    print(SCRIPT_VERSION)
    print(SCRIPT_AUTHOR)
    print()

    localTime = GetTime('LOCAL')
    print("Local Time:   ", localTime)

    utcTime = GetTime('UTC')
    print("UTC Time:     ", utcTime)

    invalidTime = GetTime('BAD')
    print("Invalid Time: ", invalidTime)


    main()


# End of Script Main




