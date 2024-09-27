import pandas as pd
ecom = pd.read_csv('C:/Users/karki/OneDrive/Desktop/ML PRAC/ML-Learning-Journey/04-exercise-panda/EcommercePurchases.csv')


print(ecom.head())
print(ecom.info())
print(ecom['Purchase Price'].mean()) #bracket wala kyuki name mai space tha
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())
print(ecom[ecom['Language']=='en'].count())
print(ecom['AM or PM'].value_counts())
print(ecom[ecom["Credit Card"] == 4926535242672853]['Email'])
#How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print(ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count())
#How many people have a credit card that expires in 2025?
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25'))
#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))