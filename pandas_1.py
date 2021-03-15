# PANDAS #
# INFO: https://www.geeksforgeeks.org/python-pandas-dataframe/ #
import pandas as pd

# Hash to DataFrame
# All the narray must be of the same length
hash_1 = {'col1': [1, 2], 'col2': [3, 4]}
df_1 = pd.DataFrame(data=hash_1)

# List to DataFrame
lst_2 = ['I', 'am', 'learning', 'pandas',
    'and', 'it', 'is', 'cool']
df_2 = pd.DataFrame(lst_2)

# Column Selection
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
    'Age':[27, 24, 22, 32],
    'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
    'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
df_data = pd.DataFrame(data)
print(df_data[['Name', 'Qualification']])

