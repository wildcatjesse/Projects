print("\nJesse Garcia\n" +
      "9/25/22\n" +
      "Scripting Assignment 8 \n\n\n")

import sys
import re
from binascii import hexlify
from prettytable import PrettyTable

# File Chunk Size
CHUNK_SIZE = 4096

# regular expressions


wPatt = re.compile(b'[a-zA-Z]{5,15}')
x = PrettyTable()
x.field_names = ["String", "Count"]

#re-order by descending values function
def descend_dict(d, reverse = False):
    return dict(sorted(d.items(), key = lambda y: y[1], reverse = reverse))

# Create empty lists
stringList = []

# reading the mem file, sending strings to list
with open('mem.raw', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if not chunk:
            break
        else:
            unique_strings = wPatt.findall(chunk)
            for eachString in unique_strings:
                stringList.append(eachString)


#starting a dictioanry to crate string and value pairs for counts
stringDictionary = {}
print("\nPossible strings\n")

#loops through the
for i in stringList:
    lowerCaseString = i.lower()
    try:
        occurrances = stringDictionary[lowerCaseString]
        occurrances += 1
        stringDictionary[lowerCaseString] = occurrances
    except:
        stringDictionary[lowerCaseString] = 1

#re-order by descending values
descending_dict = descend_dict(stringDictionary, True)


#loop through the re-ordered dict and print
# items with 15 or more counts for better viz in output
for key, value in descending_dict.items():
    if value > 14:
        x.add_row([key,value])
print(x)





#%%
