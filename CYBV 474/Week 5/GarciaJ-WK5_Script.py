# Script Module Importing


# Python Standard Library Modules
import os           # Operating/Filesystem Module
import time         # Basic Time Module
import re
import pandas as pd
import numpy as np

# Import 3rd Party Modules

# End of Script Module Importing


# Psuedo Constants
SCRIPT_NAME    = "Script: Week 5 Assignment"
SCRIPT_VERSION = "Version 3.0"
SCRIPT_AUTHOR  = "Author: Jesus Garcia"
# End of Script Constants


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

#stop words function
def stop_words(doc):
    with open(f"{doc}", 'r') as stops:
        stopWords = stops.read()

    STOP_WORDS = set(stopWords.split())
    return STOP_WORDS


def normalize_text(text):
    '''
    Function that will take the speech and normalize it before word counts
    '''
        # make all text lowercase
    text = text.lower()
    content = re.sub("[^a-z]", ' ', text)
    wordList = set(content.split())
    return wordList

def word_count(text,vocabulary):
    '''
    Uses the same format as the previous to be able to loop through the speeches.
    :param num:
    :param vocabulary:
    :return list of word counts:
    '''
    word_counts = []
    word_count_dict = {}
    for w in vocabulary:
        if len(w) > 2:
            word_count_dict[w] = text.count(w)
    word_counts.append(word_count_dict)
    return word_count_dict








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

    # storing stoip words as a set in stops variable
    stops = stop_words("STOP_WORDS.txt")
    #print(stops)
    # number of speeches
    number_of_speeches = range(5)

    for i in number_of_speeches:
        with open(f"SPEECH{i+1}.txt", 'r') as book:
            text = book.read()
            normal = normalize_text(text)
            #print(normal, '\n')
            vocabulary = normal - stops
            #print(f'{i} vocabulary,{vocabulary}\n')
            # store the dictionary that has occurrence and word
            count_dict = word_count(text,vocabulary)
            #print(count_dict)
            # creating the df from our wordcount dict
            df = pd.DataFrame.from_dict(count_dict, orient='index', columns = ["Occurrence"])
            #creating the freq list for the calculations
            #print(count_dict.items(), '\n')
            freq = []
            for word,occur in count_dict.items():
                freq.append(round(((occur / len(normal)) * 100.0), 2))
            #print(freq)
            df['Frequency'] = freq
            df = df.sort_values('Occurrence',ascending=False)
            df = df.head(25)
            df.to_csv(f'SPEECH{i+1}.csv',encoding='utf-8')
            print(df)








    


# End of Script Main




