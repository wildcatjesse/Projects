# Script Module Importing


# Python Standard Library Modules
import os           # Operating/Filesystem Module
import time         # Basic Time Module
import csv

# Import 3rd Party Modules
import pandas as pd
import numpy

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


    '''
        Creating a Panda Dataframe from a CSV File
    '''

    print("Assignment 2 - Week 2")
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)

    # Reading the csv file and storing as dataframe called df
    print("\nCreate a Dataframe from the provided csv file and display the results")
    df = pd.read_csv('ipObservations.csv')
    print("\n",df)

    #print(len(df))
    # Removing the rows with IPV6 in the 'frame-type' column
    print("\nRemoving the rows with IPV6 in the 'Frame-type' column")
    df = df.drop(df[df['FRAME-TYPE'] == 'IPV6'].index)
    print("\n",df)
    print("\n",df['DST-PORT'].value_counts())

    print("\nMap the string data to a numeric value.")
    df['FRAME-TYPE'] =  df['FRAME-TYPE'].map({'IPV4': 1, 'ARP': 2})
    df['PROTOCOL'] =    df['PROTOCOL'].map({'TCP': -1, 'UDP': -2, 'BROADCAST': -3, 'ICMP': -4})
    df['SRC-COUNTRY'] = df['SRC-COUNTRY'].map({'United States': 1,'Ireland': 2,'Russian Federation': 3,'France': 4, 'LOCAL': 5})
    df['DST-COUNTRY'] = df['DST-COUNTRY'].map({'United States': 1,'Ireland': 2,'Russian Federation': 3,'Japan': 4,'France': 5,'Netherlands': 6,'LOCAL': 7,'MULTICAST': 8, 'RESERVED': 9})
    df['SRC-PORT'] =    df['SRC-PORT'].map({'EPH': -1}).fillna(df['SRC-PORT'])
    df['DST-PORT'] =    df['DST-PORT'].map({'EPH': -1}).fillna(df['DST-PORT'])
    print("\n", df)

    print("\n Sorted Observed connections by highest first")
    df.sort_values(by=['Observed'], inplace=True, ascending=False)
    # Display the resulting table
    print("\nReset the Index field and Display the final Results")
    df.reset_index(drop=True, inplace=True)
    print("\n", df)

    print("\nSaving data frame to csv file")
    df.to_csv('Garcia-WK-2.csv')


# End of Script Main




