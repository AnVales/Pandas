# PANDAS: DATAFRAME #
# INFO: https://www.geeksforgeeks.org/python-pandas-dataframe/ #
import pandas as pd
import numpy as np

# HASH TO DATAFRAME #
# All the narray must be of the same length
hash_1 = {'col1': [1, 2], 'col2': [3, 4]}
df_1 = pd.DataFrame(data=hash_1)

# LIST TO DATAFRAME #
lst_2 = ['I', 'am', 'learning', 'pandas',
    'and', 'it', 'is', 'cool']
df_2 = pd.DataFrame(lst_2)

# COLUMN SELECTION #
data_3 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age':[27, 24, 22, 32],
    'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
df_3 = pd.DataFrame(data_3)
print(df_3[['Name', 'Qualification']])

# MAKE DATA FRAME FROM CSV FILE #
df_4 = pd.read_csv("nba.csv", index_col= "Name") 
first = df_4.loc["Avery Bradley"]
second = df_4.loc["R.J. Hunter"]

# Df_4 type: pandas.core.frame.DataFrame
print(type(df_4))
# first type: pandas.core.series.Series
print(type(first))

first_1 = df_4["Age"]
print(first_1)
first_2 = df_4.loc["Avery Bradley"]["Age"]
print(first_2)

print(first, "\n\n\n", second)

# SELECT A SINGLE COLUMN
row_1 = df_4.iloc[3]
print(row_1)

# WORKING WITH MISSING DATA #
hash_2 = {'First Score': [100, 90, np.nan, 95],
    'Second Score': [30, 45, 56, np.nan],
    'Third Score':[np.nan, 40, 80, 98]}
df_5 = pd.DataFrame(hash_2)
print(df_5.isnull())
print(df_5.notnull())
df_6 = df_5.fillna(0)
print(df_6)

# we drop rows with at least one Nan value (Null value)
print(df_5.dropna())

# ITERATE OVER ROWS AND COLUMNS #
hash_3 = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
    'degree': ["MBA", "BCA", "M.Tech", "MBA"],
    'score':[90, 40, 80, 98]}
df_7 = pd.DataFrame(hash_3)

for i, j in df_7.iterrows():
    print(i, j)
    print()

columns = list(df_7)
print(columns)

for i in columns:

    #  print the third element of the column
    print (df_7[i][2])