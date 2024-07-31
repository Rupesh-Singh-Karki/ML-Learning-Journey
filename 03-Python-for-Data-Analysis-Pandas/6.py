#operations
import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

# Info on Unique Values
df['col2'].unique() #gives all the unique value at that col
df['col2'].nunique() #number of unique
df['col2'].value_counts()

# Selecting Data

#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
# 	col1	col2	col3
#3	 4	     444	xyz

# Applying Functions
def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len) #display lenth of each item in that col
df['col1'].sum() #gives sum of all the element in that col

#permanently delete a col
del df['col1']

# Get column and index names:
df.coloumns
df.index

df.sort_values(by='col2') #inplace=False by default

# Find Null Values or Check for Null Value
df.isnull() #put true in table if empty


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
# 	A	B	C	D
# 0	foo	one	x	1
# 1	foo	one	y	3
# 2	foo	two	x	2
# 3	bar	two	y	5
# 4	bar	one	x	4
# 5	bar	one	y	1

df.pivot_table(values='D',index=['A', 'B'],columns=['C'])

# 	     C	 x	y
# A	     B		
# bar	one	4.0	1.0
#       two	NaN	5.0
# foo	one	1.0	3.0
#       two	2.0	NaN