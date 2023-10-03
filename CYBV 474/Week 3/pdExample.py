'''
Panda Usage Example
Network Data
1) Creating a Panda Dataframe from a csv file
2) Creating new Panda Dataframes from a subset of Columns
3) Eliminating Rows with certain values
4) Creating simple Horizonal Plots to Compare the data

Professor Hand
September 2023
'''

# Import 3rd Part Libraries
import pandas as pd
import matplotlib.pyplot as plt

def main():
  
    ''' Panda Mainpulations Example '''
    
    # Set no display limits and a large width
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)   
    pd.set_option('display.width', 2000)
     
    # Create a dataframe from the IP-CONNECT.CSV File
    df = pd.read_csv("IP-CONNECT.csv")
    print("\n",df.columns)

    
    print("\nSample Dataframe")
    print(df.head(10))

    # Filter out ipV6 Rows
    df = df[df.ipV6 == 0]
    print("\n",df.head(10))
    
    # Filter out TCP observations count < 30
    df = df[df.TCP >= 30]
    print("\n",df.head(10))
    
    colNdx = df.columns
    print("\n",colNdx)
    
    # Create a new Dataframe with only the Connection and TCP Columns
    # and transpose the rows and columns

    dfTCP = pd.DataFrame([df.CONNECTION, df.TCP]).transpose()
    print("this is transposed\n")
    print("\n",dfTCP.head(10))

    '''
    Setup for plotting the results
    select columns
    set x and y labels
    set the plot title
    show the plot
    '''
    
    colNdx = dfTCP.columns
    print("\n", colNdx)
    
    plt.barh(dfTCP[colNdx[0]], dfTCP[colNdx[1]], color='blue')
    plt.xlabel('TCP OBSERVATIONS')
    plt.ylabel('CONNECTION')
    plt.title('CONNECTION vs TCP')
    plt.show()  


# Main Program Starts Here
#===================================

if __name__ == '__main__':
    main()

