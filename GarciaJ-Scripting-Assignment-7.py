print("\nJesse Garcia\n" +
      "9/25/22\n" +
      "Scripting Assignment 7 \n\n\n")

import sys
import re
from binascii import hexlify 

# File Chunk Size
CHUNK_SIZE = 1024

# regular expressions

ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')
uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')

# Create empty lists
emailList = []
urlList = []
# Read in the binary file test.bin
with open('mem.raw', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            emails = ePatt.findall(chunk)
            urls = uPatt.findall(chunk)

            for eachEmail in emails:
                if eachEmail in emailList:
                    pass
                else:
                    emailList.append(eachEmail)
            for eachUrl in urls:
                if eachUrl in urlList:
                    pass
                else:
                    urlList.append(eachUrl)
        else:
            break
        
print("\nPossible e-mails\n")
for eachPossibleEmail in emailList:
    print(eachPossibleEmail)
print("\nPossible urls\n ----------------------")
for eachpossibleUrl in urlList:
    print(eachpossibleUrl)


#%%
