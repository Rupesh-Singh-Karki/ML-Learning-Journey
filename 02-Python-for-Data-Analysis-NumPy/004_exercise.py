import numpy as np

arr0 = np.zeros(10)
arr1 = np.ones(10)
arr5 = np.arange(0,10)
arr5[:] = 5
arr10 = np.arange(10,51)
arreven = arr10.copy()
arreven = arreven[arreven%2 == 0] #or np.arange(10,51,2)

matrix3 = np.arange(9).reshape(3,3)

matrixid = np.eye(3)

n = np.random.rand(1)

n25 = np.random.randn(25)

# nn = np.linspace(0,1,100).reshape(10,10)
nn = np.arange(1,101).reshape(10,10) / 100

nn1 = np.linspace(0,1,20)


#Numpy indexing and soution
mat = np.arange(1,26).reshape(5,5)
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

new = mat[2:5,1:5]
new1 = mat[3,4]
new2 = mat[0:3,1:2]

value = mat.sum()
value1 = mat.std()
value2 = mat.sum(axis=0) #axis=0 specifies the direction along which the sum is to be calculated.
# This specifies that the sum should be calculated along the rows for each column
# corresponds to the vertical direction (i.e., down the rows).
# Operation Breakdown:
# Column 1: Sum of elements in the first column (1 + 6 + 11 + 16 + 21) = 55
# Column 2: Sum of elements in the second column (2 + 7 + 12 + 17 + 22) = 60
# Column 3: Sum of elements in the third column (3 + 8 + 13 + 18 + 23) = 65
# Column 4: Sum of elements in the fourth column (4 + 9 + 14 + 19 + 24) = 70
# Column 5: Sum of elements in the fifth column (5 + 10 + 15 + 20 + 25) = 75
print(value2)