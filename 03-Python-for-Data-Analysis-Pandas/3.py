import numpy as np
import pandas as pd

#missing data
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

# 	A	B	C
# 0	1.0	5.0	1
# 1	2.0	NaN	2
# 2	NaN	NaN	3

df.dropna()
# it removes any row that contains at least one NaN value
df.dropna(axis=1) #any col with nan
df.dropna(thresh=2) #thresh: Require that many non-NaN values to retain the row/column.

df.fillna(value = 'FILL VALUE')
# 	A	B	C
# 0	1	5	1
# 1	2	FILL VALUE	2
# 2	FILL VALUE	FILL VALUE	3

df['A'].fillna(value=df['A'].mean())
# 0    1.0
# 1    2.0
# 2    1.5  yaha mean le liya 1 and 2 ka