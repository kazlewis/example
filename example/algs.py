import numpy as np
import time

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    First, check to ensure array x is not empty and composed of only numpy-based integers. 
    Then, loop through once and check pairwise to see if the next integer is larger 
    (ignoring equality to reduce number of total assignments), and if it is larger, then switch the two. 
    """
    start = time.time()
    
    if not x.size:
        return x
    
    elif all(isinstance(item, np.int64) for item in x):
        for i in range(len(x)):
            for j in range(len(x) - i - 1):
                if x[j] > x[j+1]:
                    t = x[j]
                    x[j] = x[j+1]
                    x[j+1] = t
    else: 
        return 'input is not a numeric array of integers'
        
    end = time.time()
    print ('bubblesort of array size ' + str(len(x)) + ' took ' + str(end - start) + ' seconds to complete')
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    """
    



    assert 1 == 2
    return

