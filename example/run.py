# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
from .algs import quicksort, bubblesort

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    
    # Ignore trivial, empty arrays, and non-numeric arrays
    if not x.size:
        return x
    if x.size == 1:
        return x
    if not all(isinstance(item, np.float64) for item in x):
        return 'input is not a numeric array'
    
    print("Unsorted input: ", x)

    print("Bubble sort output: ", bubblesort(x))
    print("Quick sort output: ", quicksort(x))
