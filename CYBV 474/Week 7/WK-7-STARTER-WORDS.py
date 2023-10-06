'''
WK 7
STARTER SCRIPT
'''
# PSUEDO CONTANTS
'''
Assumes that the debateRaw.txt file is in the 
same folder as the script
'''
from nltk.corpus import stopwords
stops = set(stopwords.words('english'))

DEBATE_FILE = "speechByCandidate.csv"    

topWords = {}

# take second element for sort
def CountElement(elem):
    return elem[1]

with open(DEBATE_FILE) as debate:
    for eachLine in debate:
        
        eachLine = eachLine.lower()
        lineList = eachLine.split(',')
        wordList = lineList[1].split()
        
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
    
    print(type(topWordList[:20]))

                

