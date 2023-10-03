# Script Module Importing


# Python Standard Library Modules
import os           # Operating/Filesystem Module
import time         # Basic Time Module

import numpy as np
# Import 3rd Party Modules
import pingparsing

# End of Script Module Importing


# Psuedo Constants
SCRIPT_NAME    = "Script: Week 1 Assignment"
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

    # creating
    WEBSITES = {
    #'capost.com'      : 1,
    #'cageneral.com' : 2,
    #'cadepot.com'   : 3
    'wuhsd.org'      : 1,
    'chs.wuhsd.org' : 2,
    'replit.com'   : 3
    }

    siteinfo = []
    # To get you started
    for url, id in WEBSITES.items():
        print()
        pingParser = pingparsing.PingParsing()  # create a parser object
        txObj = pingparsing.PingTransmitter()  # create a transmitter object
        txObj.destination = url  # assign the target URL
        txObj.count = 1  # define the number of ping packets

        pingResults = txObj.ping()  # perform the ping of the target url

        pingResultDict = pingParser.parse(pingResults).as_dict()  # convert the results into a dictio

        # indivdual site list of values
        sitelist= []
        sitelist.append(id)
        for key, value in pingResultDict.items():  # print out the contents of each field
            #print(key, value)
            if value != None :
                sitelist.append(value)
            else:
                pass

        siteinfo.append(sitelist)

    print(f'The list: \n{siteinfo}\n\n')

    # converting the list to a numpy array
    npArray = np.array(siteinfo)
    print(f'The Numpy Array: \n{npArray}')


    # End of Script Main




