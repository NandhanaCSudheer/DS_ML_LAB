# 1. Add a New Column 
import pandas as pd  
df = pd.read_csv("students.csv")  
df["Grade"] = ["A", "A+", "B"]  
print(df) 

# 2.Display the first row and first column 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df.iloc[0, 0]) 

# 3.Display all rows and the first column 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df.iloc[:, 0]) 

# 4.Display all rows and the first two columns 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df.iloc[:, 0:2]) 

# 5.Select rows using iloc 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df.iloc[0:3]) 

# 6.Filter students with marks greater than 80 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df[df["Marks"] > 80]) 

# 7.Find unique values 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df["Department"].unique()) 

# 8.Count unique values 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df["Department"].nunique()) 

# 9.Rename a column 
import pandas as pd 
df = pd.read_csv("students.csv") 
df.rename(columns={"Marks": "Score"}, inplace=True) 
print(df) 

# 10.Display the Last Two Rows 
import pandas as pd 
df = pd.read_csv("students.csv") 
print(df.iloc[-2:])

# 11. Delete a Row 
import pandas as pd 
df = pd.read_csv("students.csv") 
df = df.drop(0) 
print(df) 

# 12.Replace Values 
import pandas as pd 
df = pd.read_csv("students.csv") 
df["Marks"] = df["Marks"].replace(85, 90) 
print(df) 

# 13. Delete Multiple Columns 
import pandas as pd 
df = pd.read_csv("students.csv") 
df = df.drop(["Age", "Marks"], axis=1) 
print(df) 

# 14. Export to Excel  
import pandas as pd 
df = pd.read_csv("students.csv") 
df.to_excel("students.xlsx", index=False) 
print("Excel file created successfully.") 

# 15. Generate a Series of Dates 
import pandas as pd 
dates = pd.date_range( start='2021-05-01', end='2021-05-12' ) 
print(dates) 

# 16. Convert a List into a Series 
import pandas as pd 
x = [2, 4, 6, 8, 10, 12] 
s = pd.Series(x) 
print(s) 

# 17. Find Average Salary by Occupation 
import pandas as pd 
df = pd.read_csv("employee.csv") 
print(df.head()) 
avg_salary = df.groupby('Occupation')['Salary'].mean() 
print("Average salary per occupation:") 
print(avg_salary) 

# 18. Fill NaN Values with Zero 
import pandas as pd 
df = pd.read_csv("employee1.csv") 
print("Original dataset:") 
print(df.head()) 
df = df.fillna(0) 
print("Dataset after filling null values:") 
print(df.head(10))

# 19. Merge Two DataFrames 
import pandas as pd 
data1 = [     [1, 'Karan', 5000],     [2, 'Rohit', 10000],     [3, 'Sahil', 6000],     [4, 'Aryan', 8000] ] 
df1 = pd.DataFrame(data1,columns=['eid', 'ename', 'stipend']) 
data2 = [     [1, 'intern'],     [2, 'senior staff'],     [3, 'junior staff'],     [4, 'junior staff'] ] 
df2 = pd.DataFrame(data2,columns=['eid', 'position']) 
df = pd.merge(df1, df2, on='eid', how='inner') 
print(df)   

# 20. Convert a Dictionary into a DataFrame 
import pandas as pd 
data = {     'Name': ['Karan', 'Rohit', 'Sahil'],     'Age': [20, 21, 22],     'Salary': [5000, 10000, 6000] } 
df = pd.DataFrame(data) 
print(df) 