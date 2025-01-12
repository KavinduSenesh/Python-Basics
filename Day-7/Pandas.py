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

# here we are adding two raws to the dataframe
df2.loc['day4'] = [500, 60] 
df2.loc['day5'] = [600, 70]
print(df2)

# here we are deleting the row with index 'day4' from the dataframe	
filet = df2.drop('day4', axis=0, inplace=True)
print(filet)

# here we are deleting the column 'calories' from the dataframe
# filet = df2.drop('calories', axis=1, inplace=True)
# print(filet)

# here we are accessing the row with index 'day2'
print(df2.loc['day2'])
# here we are accessing the row with index 1
print(df2.iloc[1])

# here we are accessing the column 'calories' of the dataframe
print(df2['calories'])

# number of rows and columns in the dataframe
print(df2.shape)

# number of elements in the dataframe
print(df2.size)

# data type of the dataframe
print(df2.dtypes)

# here we print the columns of the dataframe
print(df2.columns)

# here we convert the dataframe to a list 
print(list(df2.columns))

# here we convert the dataframe to a numpy array
new_array = df2.values
print(new_array)
print(type(new_array))

# here we print the length of the dataframe
print(len(df2))

# here we print the mean of the dataframe
print(df2.mean())

# here we print the mean of the column 'calories' of the dataframe
print(df2['calories'].mean())



# you are a dara analyst for a retail company and the cpmpany has given you with the following table containing the sales data 

# Task - use pandas to load the above table into a dataframe
#        add a new column total revenue that calculates the totol revenue for each order
#        identitfy the best selling product/products 

# OrderId     product             category      quantity    price per unit     
#  101        laptop            electronics      2            1000
#  102        smartphones       electronics      3            500
#  103        desk chair         furniture       10           150
#  104        monitors          electronics      4            200
#  105        book shelf         furniture       2            300

data = {
    'orderId': [101, 102, 103, 104, 105],
    'product': ['laptop', 'smartphones', 'desk chair', 'monitors', 'book shelf'],
    'category': ['electronics', 'electronics', 'furniture', 'electronics', 'furniture'],
    'quantity': [2, 3, 10, 4, 2],
    'pricePerUnit': [1000, 500, 150, 200, 300]
}

df3 = pd.DataFrame(data)

# here we are adding a new column 'totalRevenue' to the dataframe
df3['totalRevenue'] = df3['quantity'] * df3['pricePerUnit']
print(df3)

# here we are filtering the dataframe to get the best selling product
filtered_df = df3[df3['totalRevenue'] == df3['totalRevenue'].max()]
print(filtered_df)

# here we are sorting the dataframe by the column 'totalRevenue'
sorted_df = df3.sort_values(by='totalRevenue')
print(sorted_df)

# here we are adding new raws
print(df2)

df4 = pd.read_csv('D:\GDSE 68\Python\customers-100.csv')
print(df4)

df5 = pd.read_json('D:\GDSE 68\Python\example_2.json')
print(df5)