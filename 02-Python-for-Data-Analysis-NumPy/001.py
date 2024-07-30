import numpy as np

l = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [1,2,3]
array1 = np.array(l2)
array2d = np.array(l)

#also we can use
np.arange(0,10) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.arange(0,11,2) #array([ 0,  2,  4,  6,  8, 10])

#genrate arrays of zeroes or ones
np.zeros(3)
array0 = np.zeros((5,5)) #[[0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]]

np.ones((5,5))

#linespace returns evenly spaced number over a specified interval
np.linspace(0,10,3) #give array with three elements which will be evenly spaced betweeen 0 and 10 inclusively


np.eye(4) #creates an identity matrix

#rand - create an array of th egiven shape and populate it with random between 0 and 1
#distribution is uniform
np.random.rand(2)
np.random.rand(5,5)


#randn -  Gaussian distribution or standard normal distribution
np.random.randn(2)
np.random.randn(5,5)

# randint
# Return random integers from low (inclusive) to high (exclusive).

#Array attributes and methods
arr = np.arange(25)
ranarr = np.random.randint(0,50,10) #creates a random array with size 10 and elements belongs to [0,50)

#reshape - returns an array containing the same data with a new shape
arr.reshape(5,5) #here transforms 1d array to 2d by putting elements to coloumn wise

#max,min,argmax,argmin
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax
arr.max()
arr.argmax()

#shape - attributes that array have (not a method)
arr.reshape(1,25)
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#         17, 18, 19, 20, 21, 22, 23, 24]])

arr.reshape(1,25).shape
# (1,25)


#dtype - grab the data type of the object in the array
print(arr.dtype) #output - int64
