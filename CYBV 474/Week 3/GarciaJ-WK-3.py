# Script Module Importing


# Python Standard Library Modules
import os           # Operating/Filesystem Module
import time         # Basic Time Module
import csv

# Import 3rd Party Modules
import pandas as pd
import numpy
import matplotlib.pyplot as plt

# End of Script Module Importing


# Psuedo Constants
SCRIPT_NAME    = "Script: Week 3 Assignment"
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

def main():
    # Reading the csv file and storing as dataframe called df
    print("\nCreate a Dataframe from the provided csv file and display the results")
    df = pd.read_csv('IP-CONNECT.csv')
    print("\n", df.head(10))

    # print(len(df))
    # Removing the rows with with ipv6 connections
    print("\nRemoving the rows with  IPV6 addresses")
    df = df[df.ipV6 == 0]
    print("\n", df.head(10).sort_values(by="ipV4", ascending=True))

    # Aggregate data based on 'CONNECTION'
    df = df.groupby('CONNECTION').sum().reset_index()



    # Create a new Dataframe with only the Connection and individual column
    # and transpose the rows and columns

    dfTCP = pd.DataFrame([df.CONNECTION, df.TCP]).transpose()
    dfTotal = pd.DataFrame([df.CONNECTION, df.TOTAL]).transpose()
    dfipV4 = pd.DataFrame([df.CONNECTION, df.ipV4]).transpose()
    dfUDP = pd.DataFrame([df.CONNECTION, df.UDP]).transpose()
    dfARP = pd.DataFrame([df.CONNECTION, df.ARP]).transpose()
    dfICMP = pd.DataFrame([df.CONNECTION, df.ICMP]).transpose()
    dfIGMP = pd.DataFrame([df.CONNECTION, df.IGMP]).transpose()
    dfCAST = pd.DataFrame([df.CONNECTION, df.CAST]).transpose()
    dfINTERNAL = pd.DataFrame([df.CONNECTION, df.INTERNAL]).transpose()
    dfDOMESTIC = pd.DataFrame([df.CONNECTION, df.DOMESTIC]).transpose()
    dfFOREIGN = pd.DataFrame([df.CONNECTION, df.FOREIGN]).transpose()
    dfHOSTILE = pd.DataFrame([df.CONNECTION, df.HOSTILE]).transpose()

    # PRINTING THE 2D data framess and creating the plot for it.
    # using mat plot lib
    print('\nConnection with Total\n')
    print("\n", dfTotal)
    colNdx_Total = dfTotal.columns
    print("\n", colNdx_Total)

    plt.barh(dfTotal[colNdx_Total[0]], dfTotal[colNdx_Total[1]], color='blue')
    plt.xlabel('Total')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs Total')
    plt.savefig("outputtot.jpg")
    plt.show()

    # Ipv4
    print('\nConnection with ipv4\n')
    print("\n", dfipV4)
    colNdx_ipV4 = dfipV4.columns
    print("\n", colNdx_ipV4)

    plt.barh(dfipV4[colNdx_ipV4[0]], dfipV4[colNdx_ipV4[1]], color='blue')
    plt.xlabel('ipV4')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs ipV4')
    plt.savefig("outputipv4.jpg")
    plt.show()

    # TCP
    print('\nConnection with TCP\n')
    print("\n", dfTCP)
    colNdx_TCP = dfTCP.columns
    print("\n", colNdx_TCP)

    plt.barh(dfTCP[colNdx_TCP[0]], dfTCP[colNdx_TCP[1]], color='blue')
    plt.xlabel('TCP')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs TCP')
    plt.savefig("outputtcp.jpg")
    plt.show()

    # UDP
    print('\nConnection with UDP\n')
    print("\n", dfUDP)
    colNdx_UDP = dfUDP.columns
    print("\n", colNdx_UDP)

    plt.barh(dfUDP[colNdx_UDP[0]], dfUDP[colNdx_UDP[1]], color='blue')
    plt.xlabel('UDP')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs UDP')
    plt.savefig("outputudp.jpg")
    plt.show()

    # ARP
    print('\nConnection with ARP\n')
    print("\n", dfARP)
    colNdx_ARP = dfARP.columns
    print("\n", colNdx_ARP)

    plt.barh(dfARP[colNdx_ARP[0]], dfARP[colNdx_ARP[1]], color='blue')
    plt.xlabel('ARP')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs ARP')
    plt.savefig("outputarp.jpg")
    plt.show()

    # ICMP
    print('\nConnection with ICMP\n')
    print("\n", dfICMP)
    colNdx_ICMP = dfICMP.columns
    print("\n", colNdx_ICMP)

    plt.barh(dfICMP[colNdx_ICMP[0]], dfICMP[colNdx_ICMP[1]], color='blue')
    plt.xlabel('ICMP')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs ICMP')
    plt.savefig("outputicmp.jpg")
    plt.show()

    # igmp
    print('\nConnection with IGMP\n')
    print("\n", dfIGMP)
    colNdx_IGMP = dfIGMP.columns
    print("\n", colNdx_IGMP)

    plt.barh(dfIGMP[colNdx_IGMP[0]], dfIGMP[colNdx_IGMP[1]], color='blue')
    plt.xlabel('IGMP')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs IGMP')
    plt.savefig("outputigmp.jpg")
    plt.show()

    # cast
    print('\nConnection with CAST\n')
    print("\n", dfCAST)
    colNdx_CAST = dfCAST.columns
    print("\n", colNdx_CAST)

    plt.barh(dfCAST[colNdx_CAST[0]], dfCAST[colNdx_CAST[1]], color='blue')
    plt.xlabel('CAST')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs CAST')
    plt.savefig("outputcast.jpg")
    plt.show()

    # Internal
    print('\nConnection with INTERNAL\n')
    print("\n", dfINTERNAL)
    colNdx_INTERNAL = dfINTERNAL.columns
    print("\n", colNdx_INTERNAL)

    plt.barh(dfINTERNAL[colNdx_INTERNAL[0]], dfINTERNAL[colNdx_INTERNAL[1]], color='blue')
    plt.xlabel('INTERNAL')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs INTERNAL')
    plt.savefig("outputint.jpg")
    plt.show()

    # DOMESTIC
    print('\nConnection with DOMESTIC\n')
    print("\n", dfDOMESTIC)
    colNdx_DOMESTIC = dfDOMESTIC.columns
    print("\n", colNdx_DOMESTIC)

    plt.barh(dfDOMESTIC[colNdx_DOMESTIC[0]], dfDOMESTIC[colNdx_DOMESTIC[1]], color='blue')
    plt.xlabel('DOMESTIC')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs DOMESTIC')
    plt.savefig("outputdom.jpg")
    plt.show()

    # FOREIGN
    print('\nConnection with FOREIGN\n')
    print("\n", dfFOREIGN)
    colNdx_FOREIGN = dfFOREIGN.columns
    print("\n", colNdx_FOREIGN)

    plt.barh(dfFOREIGN[colNdx_FOREIGN[0]], dfFOREIGN[colNdx_FOREIGN[1]], color='blue')
    plt.xlabel('FOREIGN')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs FOREIGN')
    plt.savefig("outputfor.jpg")
    plt.show()

    # HOSTILE
    print('\nConnection with HOSTILE\n')
    print("\n", dfHOSTILE)
    colNdx_HOSTILE = dfHOSTILE.columns
    print("\n", colNdx_HOSTILE)

    plt.barh(dfHOSTILE[colNdx_HOSTILE[0]], dfHOSTILE[colNdx_HOSTILE[1]], color='blue')
    plt.xlabel('HOSTILE')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs HOSTILE')
    plt.savefig("outputhostile.jpg")
    plt.show()
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

    print("Assignment 3 - Week 3")
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)

    main()



# End of Script Main




