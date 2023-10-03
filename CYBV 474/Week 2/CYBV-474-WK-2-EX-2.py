'''
CYBV-474
August 2023
Professor Hand

Panda Simple Dataframe Example
WK-2
'''

# Standard Library Imports
    
# 3rd Party Library Imports
print("Please wait, importing libraries")
import pandas as pd        # import Pandas 3rd party library

# Main Script Starts Here
if __name__ == '__main__':

    '''
    Example 3 - Processing IP Observations from a csv file
    '''
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)

    
    print('\n')

    # Create a Panda Dataframe from a CSV File
    print("Create a Dataframe from the provided csv file and display the results")
    testDF = pd.read_csv (r'CONNECTIONS.CSV')
    print("\n",testDF)
    
    print("\nMap the non-numeric data to numermic values and display the results")
    # MAPS strings and Bool to integer values  
    testDF['WEEKEND']     = testDF['WEEKEND'].map({False:0 ,True:1}) 
    testDF['DAY-TIME']    = testDF['DAY-TIME'].map({False:0 ,True:1})           
    testDF['NIGHT-TIME']  = testDF['NIGHT-TIME'].map({False:0 ,True:1})     
    testDF['SRC-Country'] = testDF['SRC-Country'].map({'LOCAL':1 ,'FOREIGN':2, 'FOREIGN-HOSTILE':3})  
    testDF['DST-Country'] = testDF['DST-Country'].map({'LOCAL':1 ,'FOREIGN':2, 'FOREIGN-HOSTILE':3})         
    testDF['SRC-Port']    = testDF['SRC-Port'].map({'EPH': -1 })         
    testDF['DST-Port']    = testDF['DST-Port'].map({'EPH': -1 })             
    # Display the resulting table

    print("\n",testDF)

    

    

