import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    np_arr = np.array(arr,float)
    return np_arr

    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)