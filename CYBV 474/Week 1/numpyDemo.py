'''
numpy arrays 
CYBV-474
December 2020
Professor Hosmer

NumPy Examples

'''

import numpy as np     # import numpy 3rd party library

# Main Script Starts Here

if __name__ == '__main__':

    '''
    Example 1 - Create a two dimensional arrary of random integers
                with values of 1-99
    '''
    npArray = np.random.randint(1,100, size=(10,2))
    print(npArray)
    
    ''' 
    Example 2 - apply simple mathematical operations 
                to the npArray
    '''
    print("\nSome simple math")
    print("Sum:    ",   npArray.sum())
    print("Max:    ",   npArray.max())
    print("\nSqrt:     \n", np.sqrt(npArray))
    print("\nSquare:   \n", np.square(npArray))
    print("\nTangent:  \n", np.tan(npArray))
    
    '''
    Example 3 - Convert a list to a numpy array
    '''
    print("\nConvert a List to a numpy array")
    myList = []
    myList.append([1,7,119,140,0])
    myList.append([2,6,44,1,1])
    
    npArray = np.array(myList)
    print(npArray)
    
