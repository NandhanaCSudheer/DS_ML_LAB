import pandas as pd

# arr = [12,34,5,43,67,98,3]
# s = pd.Series(arr)
# print(s)

# print(pd.date_range("2021-05-01","2021-05-31"))

# d = {"Name":["A","B","C"],"Age":[21,22,23]}
# data = pd.DataFrame(d)
# print(data)

# d = [["A",21],["B",22],["C",23]]
# data = pd.DataFrame(d,columns = ["Name","Age"])
# print(data)

data = pd.read_csv("pgm4.csv")
# print(data)

# print(data.head(2))
# print(data.iloc[-2:])
# print()
# print(data.iloc[0,0:1])
# print()
# print(data.iloc[:,0:2])

emp = {"EID":[101,102,103,104],"Name":["Anu","Arun","Meera","Rahul"],"Occupation":["Developer","Tester","Developer","Designer"],"Salary":[30000,25000,35000,28000]}
des = {"EID":[101,102,103,104],"Designation":["Senior","Junior","Senior","Junior"]}
e = pd.DataFrame(emp)
d = pd.DataFrame(des)
avg = e.groupby("Occupation")["Salary"].mean()
print(avg)
merged = pd.merge(e,d,how = "inner",on = "EID")
print(merged)
print(merged["EID"],merged["Name"],merged["Salary"],merged["Designation"])
merged.to_excel("merged.xlsx",index=False)
