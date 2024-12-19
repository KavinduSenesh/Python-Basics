import pandas as pd

# Create a simple DataFrame
# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects.

data = {
    'Name': ['John', 'Doe', 'Smith'],
    'Age': [28, 34, 29] 
}
df = pd.DataFrame(data)
print(df, type(df))

# here we are accessing the column 'Name' of the dataframe using loc method which is used to access the data by label
print(df.loc[1, 'Name'])
# here we are accessing the column 'Name' of the dataframe using iloc method which is used to access the data by index
print(df.iloc[1, 0])

# here we access the row 0 and 2 of the dataframe
print(df.loc[[0, 2]], type(df.loc[[0, 2]]))

newData = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

#we can change index of the dataframe by passing index parameter to the DataFrame constructor like this
df2 = pd.DataFrame(newData, index=['day1', 'day2', 'day3'])
print(df2)

print(df2.loc['day3' ,'calories'])
print(df2.iloc[2, 0])

# here we are accessing the row with index 'day2'
print(df2.loc['day2'])
# here we are accessing the row with index 1
print(df2.iloc[1])





