import pandas as pd

#GroupBy
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
# 	Company	Person	Sales
# 0	GOOG	Sam	    200
# 1	GOOG	Charlie	120
# 2	MSFT	Amy	    340
# 3	MSFT	Vanessa	124
# 4	FB	    Carl	243
# 5	FB	   Sarah	350

by_comp = df.groupby("Company")
# And then call aggregate methods off the object:
by_comp.mean() #or use df.groupby('Company').mean()

# Company	
# FB	    296.5
# GOOG	   160.0
# MSFT	   232.0

by_comp.std()
by_comp.min()
by_comp.max()
by_comp.count()
by_comp.describe()
# count mean std	min	25%	50%	75% max shows all these
by_comp.describe().transpose() #transpose lagane sai use woh vertical sai horizontal kardega
by_comp.describe().transpose()['GOOG']
