# Script Module Importing


# Python Standard Library Modules
import os           # Operating/Filesystem Module
import time         # Basic Time Module
from collections import defaultdict

# Import 3rd Party Modules
import pandas as pd

# End of Script Module Importing


# Psuedo Constants
SCRIPT_NAME    = "Script: Week 4 Assignment"
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

# Main Function
def main():
    # Reading the txt file and storing as dictionary
    print("\nCreate a Dataframe from the provided csv file and display the results")
    with open("ps.txt", 'r', encoding='utf-16le') as f:
        for line in f:
            print(line)


    #df = pd.read_csv('ps.txt')
    #print("\n", df.head(10))
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




