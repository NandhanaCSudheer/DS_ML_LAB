import pandas as pd
data = {"name":["abc","def","xyz"],"age":[22,23,24]}  # This creates a Python dictionary
df = pd.DataFrame(data)  # pd.DataFrame() converts the dictionary into a Pandas DataFrame, which looks like a table. Pandas automatically creates an index
var = {"sub":["CS","Maths","Eng","Hindi"],"dept":["CSE","Math","Language","Section"],"days":["Mon","Tues","Wed","Thur"]}
dd = pd.DataFrame(var)
print(dd)
print(df)
print(df.loc[0])   # loc is used to access data using the index label. Get the first row 