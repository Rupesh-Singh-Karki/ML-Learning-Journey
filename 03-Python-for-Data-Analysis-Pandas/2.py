#dataframes
import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(101)
# This line sets the seed for Numpy's random number generator. By specifying a seed 
# value (in this case, 101), you ensure that the random numbers generated are the same 
# every time the code is run, providing reproducibility for debugging and testing.
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
# index='A B C D E'.split(): Creates a list of strings ['A', 'B', 'C', 'D', 'E'] to be used 
# as the row indices of the DataFrame. The split() method splits the string into a list of
# substrings using spaces as delimiters.


#selection and indexing
df['W']
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794
# Name: W, dtype: float64

df[['W','Z']]
# 	   W	           Z
# A	2.706850	0.503826
# B	0.651118	0.605965
# C	-2.018168	-0.589001
# D	0.188695	0.955057
# E	0.190794	0.683509

# DataFrame Columns are just Series
type(df['W'])
# pandas.core.series.Series

df['new'] = df['W'] + df['Y']
# 	W	            X	       Y	         Z	     new
# A	2.706850	0.628133	0.907969	0.503826	3.614819
# B	0.651118	-0.319318	-0.848077	0.605965	-0.196959
# C	-2.018168	0.740122	0.528813	-0.589001	-1.489355
# D	0.188695	-0.758872	-0.933237	0.955057	-0.744542
# E	0.190794	1.978757	2.605967	0.683509	2.796762

df.drop('new',axis=1) #temporary Removing Columns
df.drop('new',axis=1,inplace=True) #actualy removes col

#similarly
df.drop('E',axis=0)

#selecting rows
df.loc['C'] #both select same row
df.iloc[2] 

#selecting subset of a row or col
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]

#condition selection
# An important feature of pandas is conditional selection using bracket notation, very similar to numpy:
df>0
df[df>0]
# 	W	         X	         Y	         Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	NaN	        NaN	        0.605965
# C	NaN	        0.740122	0.528813	NaN
# D	0.188695	NaN     	NaN	        0.955057
# E	0.190794	1.978757	2.605967	0.683509
df[df['W']>0]
# 	W	X	Y	Z
# A	2.706850	0.628133	0.907969	0.503826
# B	0.651118	-0.319318	-0.848077	0.605965
# D	0.188695	-0.758872	-0.933237	0.955057
# E	0.190794	1.978757	2.605967	0.683509
df[df['W']>0]['Y'] #In summary, this function returns the values from column 'Y' 
                   #for the rows where the values in column 'W' are greater than 0.
# A    0.907969
# B   -0.848077
# D   -0.933237
# E    2.605967
# Name: Y, dtype: float64
df[df['W']>0][['Y','X']]
# 	Y	X
# A	0.907969	0.628133
# B	-0.848077	-0.319318
# D	-0.933237	-0.758872
# E	2.605967	1.978757
df[(df['W']>0) & (df['Y'] > 1)]
	# W	X	Y	Z
# E	0.190794	1.978757	2.605967	0.683509

#more index detail

# Reset to default 0,1...n index
df.reset_index()

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
# 	W	X	Y	Z	States
# A	2.706850	0.628133	0.907969	0.503826	CA
# B	0.651118	-0.319318	-0.848077	0.605965	NY
# C	-2.018168	0.740122	0.528813	-0.589001	WY
# D	0.188695	-0.758872	-0.933237	0.955057	OR
# E	0.190794	1.978757	2.605967	0.683509	CO

df.set_index('States')
# 	   W	X	Y	Z
# States				
# CA	2.706850	0.628133	0.907969	0.503826
# NY	0.651118	-0.319318	-0.848077	0.605965
# WY	-2.018168	0.740122	0.528813	-0.589001
# OR	0.188695	-0.758872	-0.933237	0.955057
# CO	0.190794	1.978757	2.605967	0.683509

df.set_index('States',inplace=True) #requires inplace

#multi index and index heirachy

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
# The elements of this list are meant to represent the first level of a hierarchical index,
# often indicating groups or categories (in this case, two groups: 'G1' and 'G2').
inside = [1,2,3,1,2,3]
# The elements of this list are meant to represent the second level of a hierarchical index,
# often indicating subgroups or subcategories within each group defined by outside.
hier_index = list(zip(outside,inside))
# [('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

hier_index = pd.MultiIndex.from_tuples(hier_index)
# MultiIndex(levels=[['G1', 'G2'], [1, 2, 3]],
#            labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]])

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

# 		  A	            B
# 	  1	0.153661	0.167638
# G1  2	-0.765930	0.962299
#     3	0.902826	-0.537909
# G2  1	-1.549671	0.435253
#     2	1.259904	-0.447898
#     3	0.266207	0.412580

df.loc['G1'] #print whole g1
df.loc['G1'].loc[1] #print g1,s 1 of A and B

df.index.names = ['Group','Num']
# 		           A	          B
# Group	   Num		
# G1	    1	0.153661	0.167638
#           2	-0.765930	0.962299
#           3	0.902826	-0.537909
# G2	    1	-1.549671	0.435253
#           2 	1.259904	-0.447898
#           3	0.266207	0.412580


# DataFrame.xs(key, axis=0, level=None, drop_level=True)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df.xs('G1') #This will return all rows that belong to the 'G1' group from the first level of the MultiIndex
df.xs(['G1',1])
df.xs(1,level='Num')