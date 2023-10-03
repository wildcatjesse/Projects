# Script Module Importing


# import python standard libraries
import os           # Operating/Filesystem Module
import time         # Basic Time Module
from collections import Counter
import re

#import python 3rd party libs
from nltk import word_tokenize, pos_tag, FreqDist
import pandas as pd
from prettytable import PrettyTable

# End of Script Module Importing


# Psuedo Constants
SCRIPT_NAME    = "Script: Week 6 Assignment"
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

DEBATE_FILE = "debateRaw.txt"

#pd.set_option('display.max_rows', None)



def main():
    df = pd.DataFrame(columns=['Candidate', 'Response'])
    bidenText = ''
    buttText = ''
    bernieText = ''
    warrenText = ''
    amyText = ''
    bloombergText = ''
    names= set()
    with open(DEBATE_FILE) as debate:
        for eachLine in debate:
            eachLine = eachLine.lower()
            candidate = ''
            response = ''

            # Process Eachline where Biden is speaking
            if "joe biden" in eachLine[:10]:
                candidate = 'Joe Biden'
                response = eachLine[10:]
                response = re.sub("[^a-zA-Z ]", ' ', response)
                new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
                df = pd.concat([df, new_row], ignore_index=True)
                bidenText = bidenText + response
                names.add(candidate)

            elif "pete buttigieg" in eachLine[:17]:
                candidate = 'Pete Buttigieg'
                response = eachLine[17:]
                response = re.sub("[^a-zA-Z ]", ' ', response)
                new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
                df = pd.concat([df, new_row], ignore_index=True)
                buttText = buttText + response
                names.add(candidate)


            elif "bernie sanders" in eachLine[:15]:
                candidate = 'Bernie Sanders'
                response = eachLine[15:]
                response = re.sub("[^a-zA-Z ]", ' ', response)
                new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
                df = pd.concat([df, new_row], ignore_index=True)
                bernieText = bernieText + response
                names.add(candidate)

            elif "michael bloomberg" in eachLine[:18]:
                candidate = 'Michael Bloomberg'
                response = eachLine[18:]
                response = re.sub("[^a-zA-Z ]", ' ', response)
                new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
                df = pd.concat([df, new_row], ignore_index=True)
                bloombergText = bloombergText + response
                names.add(candidate)

            elif "amy klobuchar" in eachLine[:14]:
                candidate = 'Amy Klobuchar'
                response = eachLine[14:]
                response = re.sub("[^a-zA-Z ]", ' ', response)
                new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
                df = pd.concat([df, new_row], ignore_index=True)
                amyText = amyText + response
                names.add(candidate)

            elif "elizabeth warren" in eachLine[:16]:
                candidate = 'Elizabeth Warren'
                response = eachLine[16:]
                response = re.sub("[^a-zA-Z ]", ' ', response)
                new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
                df = pd.concat([df, new_row], ignore_index=True)
                warrenText = warrenText + response
                names.add(candidate)

    # Tokenize the speech
    wordsBiden = word_tokenize(bidenText)
    wordsAmy = word_tokenize(amyText)
    wordsBloom = word_tokenize(bloombergText)
    wordsBernie = word_tokenize(bernieText)
    wordsButt = word_tokenize(buttText)
    wordsWarren = word_tokenize(warrenText)

     # Apply part of speech tags to each word
    tagsBiden = pos_tag(wordsBiden)
    tagsAmy = pos_tag(wordsAmy)
    tagsBloom = pos_tag(wordsBloom)
    tagsBernie = pos_tag(wordsBernie)
    tagsButt = pos_tag(wordsButt)
    tagsWarren = pos_tag(wordsWarren)

    # Obtain counts for each tag
    countsBiden = Counter(tag for word, tag in tagsBiden)
    countsAmy = Counter(tag for word, tag in tagsAmy)
    countsBloom = Counter(tag for word, tag in tagsBloom)
    countsBernie = Counter(tag for word, tag in tagsBernie)
    countsButt = Counter(tag for word, tag in tagsButt)
    countsWarren = Counter(tag for word, tag in tagsWarren)

    # created a dictionary mapping the candidate to the dictionary of counts frequencies
    # converted the FreqDist items into an actual dictionary to that my for loop can match the columns
    candidates2 = {}
    candidates2['Joe Biden'] = dict(FreqDist(countsBiden).items())
    candidates2['Amy Klobuchar'] = dict(FreqDist(countsAmy).items())
    candidates2['Michael Bloomberg']= dict(FreqDist(countsBloom).items())
    candidates2['Bernie Sanders'] = dict(FreqDist(countsBernie).items())
    candidates2['Pete Buttigieg']= dict(FreqDist(countsButt).items())
    candidates2['Elizabeth Warren'] = dict(FreqDist(countsWarren).items())

    # Creating the columns from the keys in the counts dictionary.
    elements = []
    for tag, count in countsButt.items():
        elements.append(tag)
    df2 = pd.DataFrame(columns=elements)

    # adding the candidate column
    df2.insert(0,'Candidate',list(names))
    #can_col = df2.pop("candidate")
    df2.set_index('Candidate')

    # Verify that the keys of the dictionary match the columns of the DataFrame
    for index, row in df2.iterrows():
        # Get the candidate from the current row
        candidate = row['Candidate']

        # Get the corresponding dictionary for the candidate
        candidate_dict = candidates2.get(candidate, {})

        # Iterate through each item in the dictionary and update the DataFrame
        for key, value in candidate_dict.items():
            df2.at[index, key] = value

    print("\nPart of Speech Results\n")
    print(df2)



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




