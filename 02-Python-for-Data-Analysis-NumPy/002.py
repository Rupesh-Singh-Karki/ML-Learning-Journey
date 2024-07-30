import numpy as np

arr = np.arange(0,25)
#value selection
#index selection
arr[5]
arr[1:5] #gets all the elemts from 1 to 4

#brodcasting - Numpy arrays differ from a normal Python list because of their ability to broadcast:
arr[0:5] = 100 #array([100, 100, 100, 100, 100,   5,   6,   7,   8,   9,  10])

arr = np.arange(0,25) #reset

slice_of_Arr = arr[0:6]
slice_of_Arr[:] = 99
#now if we print our array the changes will be done in it also
# Data is not copied, it's a view of the original array! This avoids memory problems

arr_copy = arr.copy()


# Indexing a 2D array 
# The general format is arr_2d[row][col] or arr_2d[row,col]. I recommend usually using the comma notation for clarity.
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
#indexing similar to c++

# 2D array slicing
arr_2d[:2,1:] #array([[10, 15],
                    #[25, 30]])

#fancy indexing - Fancy indexing allows you to select entire rows or columns out of order,to show this, let's quickly build out a numpy array:
arr2d = np.zeros((10,10))
arr_length = arr2d.shape[1]
for i in range(arr_length):
    arr2d[i] = i #setting up an array

# fancy indexing allows the following
arr2d[[2,4,6,8]]
    #  ([[ 2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.],
    #    [ 4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.],
    #    [ 6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.],
    #    [ 8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.,  8.]])

arr2d[[6,4,2,7]]
    #  ([[ 6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.,  6.],
    #    [ 4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.,  4.],
    #    [ 2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.,  2.],
    #    [ 7.,  7.,  7.,  7.,  7.,  7.,  7.,  7.,  7.,  7.]])

#selection
arr = np.arange(1,11)

arr > 4
# array([False, False, False, False,  True,  True,  True,  True,  True,  True], dtype=bool)
bool_arr = arr>4
arr[bool_arr]
# array([ 5,  6,  7,  8,  9, 10])

arr[arr>2]
#or
x = 2
arr[arr>x]
# array([ 3,  4,  5,  6,  7,  8,  9, 10])