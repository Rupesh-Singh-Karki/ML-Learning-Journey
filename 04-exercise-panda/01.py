import pandas as pd


sal = pd.read_csv('C:/Users/karki/OneDrive/Desktop/ML PRAC/ML-Learning-Journey/04-exercise-panda/Salaries.csv')
print(sal.head())
# The head of a DataFrame refers to the first few rows of the data. It's a quick way to preview the structure,
# content, and format of the DataFrame, especially useful when working with large datasets.
print(sal.info())
# The .info() method in pandas provides a concise summary of a DataFrame, giving you essential information 
# about its structure and content.
print(sal.BasePay.mean())
print(sal.OvertimePay.max())
print(sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()])