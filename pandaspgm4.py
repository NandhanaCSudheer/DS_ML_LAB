#write a python program to print list to series conversion
# py prgm to generate a series of date from may 1 2021 to 12 may 2021.
#given a dict and 2d list ,convert both into corresponding dataframes and display it.
#given a csv file read it into a dataframe and display it.
#given a dataframe sort it by multiple columns
# given a dataframe with custom indexing convert it into default indexing and display it.
#given a dataframe select first 2 rows and output them
#given a df showing name,job,salary or people . find avg salary per job
#given a df with NaN values . fill the values with zero
#given a df sowing company names and corresponding profits. convert the values of profit column such that values  in it gt 0 are set true
# and the rest are set false
#given 2 df with one df contain emp_id ,name, and stipend. & the other df containing emp_id & designation.o/p the df containing 
#emp_id,name ,stipend ,and designation. 

# import pandas as pd
# import numpy as np

# lst = [1,2,3,4,5,6]
# var = pd.Series(lst)
# print(var)

# print(pd.date_range("2021-05-01","2021-05-12"))



# dic = {"name":["Anoop","Sweety","Nandhana"],"mark":[100,99,98]}
# l = [[1,"Anoop"],[3,"Sweety"]]
# d1 = pd.DataFrame(dic)
# d2 = pd.DataFrame(l,columns = ["Rollno","Name"])
# print(d1)
# print(d2)

# sortedd = d1.sort_values(by = "mark",ascending = True)
# print(sortedd)

# df = pd.read_csv("medal.csv")
# print(df)


# data = [
#     ['Alice',25,'new york'],
#     ['Bob',30,'Paris'],
#     ['Charlie',35,'Kattakkada']

# ]

# df = pd.DataFrame(data,columns = ['name','age','city'],index = ['p1','p2','p3'])
# dp = df.reset_index(drop = False)  #  drop = True

# print(f"{df}\n{dp}")



#given a dataframe select first 2 rows and output them

# data = [
#     ['Alice',25,'new york'],
#     ['Bob',30,'Paris'],
#     ['Charlie',35,'Kattakkada']

# ]

# df = pd.DataFrame(data,columns = ['name','age','city'])

# print(df.iloc[0:2])

#given a df showing name,job,salary of people . find avg salary per job



# dic = {
#     "name": ["Anoop", "Sweety", "Nandhana", "Rahul"],
#     "job": ["Engineer", "Teacher", "Developer", "Teacher"],
#     "salary": [50000, 45000, 60000, 70000]
# }

# print(dic)

# df = pd.DataFrame(dic)
# avg = df.groupby('job')['salary'].mean()
# print(avg)

#given a df with NaN values . fill the values with zero

# dic = {
#     "name": ["Anoop", "Sweety", "Nandhana", np.nan],
#     "job": [np.nan, "Teacher", "Developer", "Manager"],
#     "salary": [50000, 45000, 60000, np.nan]
# }

# df =  pd.DataFrame(dic)
# df = df.fillna(0)
# print(df)


#given a df sowing company names and corresponding profits. convert the values of profit column such that values 
#  in it gt 0 are set true
# and the rest are set false

# dic = {
#     "company": ["TCS", "Infosys", "Wipro", "Google", "Amazon"],
#     "profit": [50000, -20000, 30000, -10000, 70000]
# }


# df = pd.DataFrame(dic)

# df['profit'] = df['profit'] > 0
# print(df)



#given 2 df with one df contain emp_id ,name, and stipend. & the other df containing emp_id & designation.o/p the df containing 
#emp_id,name ,stipend ,and designation.

# dic1 = {
#     "emp_id": [101, 102, 103, 104],
#     "name": ["Anoop", "Sweety", "Nandhana", "Rahul"],
#     "stipend": [10000, 12000, 15000, 11000]
# }

# dic2 = {
#     "emp_id": [101, 102, 103, 104],
#     "designation": ["Developer", "Tester", "Designer", "Manager"]
# }

# df1 = pd.DataFrame(dic1)
# df2 = pd.DataFrame(dic2)
# merged = pd.merge(df1,df2,how = 'inner')
# print(merged)