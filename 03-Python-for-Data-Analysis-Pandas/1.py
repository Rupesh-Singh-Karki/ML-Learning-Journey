#series
import pandas as pd
import numpy as np

#series is similar to array difference is that it has axis labels,meaning it can be indexed by a 
#label instead of just a number location also it can hold any arbitrary python object

#creating a series
# You can convert a list,numpy array, or dictionary to a Series:

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}

pd.Series(data=my_list)
# 0    10
# 1    20
# 2    30
# dtype: int64

pd.Series(data=my_list,index=labels) #or simply pd.Series(my_list,labels)
# a    10
# b    20
# c    30
# dtype: int64

pd.Series(d)
# a    10
# b    20
# c    30
# dtype: int64

#data in a series

# Even functions (although unlikely that you will use this)
pd.Series([sum,print,len])
# 0      <built-in function sum>
# 1    <built-in function print>
# 2      <built-in function len>
# dtype: object

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])  
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])     
ser1['USA'] #gives output 1
ser1 + ser2
# if the indices do not match between the two series, the result will be NaN
# Germany    4.0
# Italy      NaN
# Japan      8.0
# USA        2.0
# USSR       NaN
# dtype: float64