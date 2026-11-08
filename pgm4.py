import pandas as pd

data = pd.read_csv("pgm4.csv")
print(data)
# data["Grade"] = ["A+","B","S","C","A+"]
# print(data)
# print(data[data["Marks"] > 80])
# print(data["Department"].unique())
# print(data["Department"].nunique())
print(data.rename(columns = {"Marks":"Score"}))
# print(data.iloc[0])
# print(data.iloc[:,0:2])
# print(data.iloc[-2:])
# group = data.sort_values(by = ["Department","Marks"], ascending=False)
# print(group)
# print(data.drop(0))
# print(data.drop("Age",axis=1))
# data["Age"] = data["Age"].replace(21,22)
# print(data)
# df = data.fillna(0)
# print(df)
# data["Marks"] = data["Marks"] > 80
# print(data)
d = [[1,"A"],[2,"B"],[3,"C"]]
dd = pd.DataFrame(d,columns = ["Rollno","Name"],index=["p1","p2","p3"])
dm = dd.reset_index(drop = True)
print(dm)