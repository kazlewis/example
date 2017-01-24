import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():

    # Test random vector
    x = np.random.rand(100)
    algs.bubblesort(x)

    # Test empty vector
    x = np.array([])
    algs.bubblesort(x)
    
    # Single element vector
    x = np.array([1.0])
    algs.bubblesort(x)

def test_quicksort():

    x = np.array([1,2,4,0,1])
    algs.quicksort(x)
    
    # Test random vector
    x = np.random.rand(100)
    algs.quicksort(x)

    # Test empty vector
    x = np.array([])
    algs.quicksort(x)
    
    # Single element vector
    x = np.array([1.0])
    algs.quicksort(x)
