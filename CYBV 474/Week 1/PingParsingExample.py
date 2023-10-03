'''

Script Purpose: PingParsing Demonstration
Script Version: 1.0 December 2020
Script Author:  Professor Hosmer, University of Arizona

Script Revision History:
Version 1.0 December 2020 Initial Version

'''

# Script Module Importing

# Python Standard Library Modules

# Import 3rd Party Modules

import pingparsing  # import the pingparsing library
                    # pip install pingparsing to install the library''

# End of Script Module Importing


# Psuedo Constants

SCRIPT_NAME    = "PingParsing Demonstration"
SCRIPT_VERSION = "Version 1.0"
SCRIPT_AUTHOR  = "Author: Professor Hosmer"

# End of Script Constants


# Script Functions

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
    
    pingParser = pingparsing.PingParsing()    # create a parser object
    txObj = pingparsing.PingTransmitter()     # create a transmitter object
    txObj.destination = "google.com"          # assign the target URL
    txObj.count = 1                           # define the number of ping packets
    
    pingResults = txObj.ping()                # perform the ping of the target url
    
    pingResultDict = pingParser.parse(pingResults).as_dict()  # convert the results into a dictionary
    siteinfo = []
    siteinfo
    for key, value in pingResultDict.items(): # print out the contents of each field
        siteinfo.append(value)
    print(siteinfo)


     
    
# End of Script Main



    
    