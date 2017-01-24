import numpy as np
import time

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    # Checks for any empty or single length vectors as well as invalid ones (non-numpy integers) occur in run.py 
    # to minimize the runtime of the algorithms.
    """
    Loop through the array  continually, starting at n+1 an onward and check pairwise to see if the next 
    integer is larger  (ignoring equality to reduce number of total assignments), and if it is larger, 
    then switch the two. 
    """
    start = time.time()
    
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                t = x[j]
                x[j] = x[j+1]
                x[j+1] = t
                    
    end = time.time()
    print ('bubblesort of array size ' + str(len(x)) + ' took ' + str(end - start) + ' seconds to complete')
    return x
    
def partition(x, lo, hi):
    """
    Partition the array starting at the front, and checking to see if any other integers in the array can we swapped
    (if they are smaller than the current partition number). Then, recurse and move down the array until it is sorted.
    """
    pivot_item = x[lo]
    left = lo + 1
    right = hi
    done = False
    
    while not done:
        while left <= right and x[left] <= pivot_item:
            left += 1
        while right >= left and x[right] >= pivot_item:
            right -= 1
        if right < left:
            done = True
        else:
            temp = x[left]
            x[left] = x[right]
            x[right] = temp
    temp = x[lo]
    x[lo] = x[right]
    x[right] = temp
    return right

def quicksortmain(x, lo, hi):
    if lo < hi:
        pivot = partition(x, lo, hi)
        quicksortmain(x, lo, pivot - 1)
        quicksortmain(x, pivot + 1, hi)
    return x
    
def quicksort(x):
    # Checks for any empty or single length vectors as well as invalid ones (non-numpy integers) occur in run.py 
    # to minimize the runtime of the algorithms. This is more of a wrapper function for partition().

    start = time.time()
    quicksortmain(x, 0, len(x) - 1)
    end = time.time()
    print ('quicksort of array size ' + str(len(x)) + ' took ' + str(end - start) + ' seconds to complete')
    return x
    