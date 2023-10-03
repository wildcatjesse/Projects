'''
CYBV-474
August 2023
Professor Hand

Basic Starter Script

'''

# Standard Library Imports
    
# 3rd Party Library Imports
print("Please wait, importing libraries")
import pandas as pd        # import Pandas 3rd party library

# Main Script Starts Here
if __name__ == '__main__':

    '''
    Creating a Panda Dataframe from a CSV File
    '''
    
    print("Assignment 2 - STARTER SCRIPT")
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)

    # Create a Panda Dataframe from a CSV File
    df = pd.read_csv(r'./DATA/ipObservations.csv')  
 
    print(df.head(10))
    

    


