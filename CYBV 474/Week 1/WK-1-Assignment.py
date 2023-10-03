'''
CYBV 474 Week One Assignment
Create a numpy array of Ping Results

Week 1 Assignment - recording ping results from CyberApolis websites

STEP One: 
Install the 3rd party library pingparsing
   from the windows command line or linux terminal
   
   pip install pingparsing

STEP Two:

Examine the pingparsing sample script demonstrating the
usage of the pingparsing library

STEP Three:
 
Create a dictionary that maps website urls to an numeric identifier
this is necessary since NumPy arrays are not designed to hold
strings, but rather only numbers.  As we proceed through the course
you will see that we need to perform this type of mapping of names
to numbers along with other tricks as most machine learning algorithms
require the use of numbers not string.

IMPORTANT NOTE: a sample is provided below, but make sure and 
                verify that you have access to the
                the websites by using the browser
                provided in your virtual learning environment

STEP 4: You are to create a Python scirpt that will:

1) Create a loop that performs ping operations against each of the WEBSITES
   contained in the dictionary WEBSITES using the pingparsing library
2) Create an empty list to hold the resulting values from each WEBSITE
3) Append the [WEBSITE #, packetsTransmitted, packetsReceived, packetsLost, minRoundTrip, maxRoundTrip, avgRoundTrip]
   for each url  (note all the values are integers)
4) Convert the list to a numpy array
5) Print out (display) the resulting numpy array

Submit two files seperate files to the assignment
1) Your python script
   script naming convention example:  WK-1-Hand.py  (no other file type will be accepted)
   The script must follow the guidelines provided in the script template
   please review the script template video for more information
2) A text file (containing the output of the numpy array

'''

WEBSITES = {
    #'capost.com'      : 1,
    #'cageneral.com' : 2,
    #'cadepot.com'   : 3
    'wuhsd.org'      : 1,
    'chs.wuhsd.org' : 2,
    'replit.com'   : 3
    }

# To get you started
for url, id in WEBSITES.items():
    print(url, id)
    ''' Your code goes here to process each website'''
    
        
    