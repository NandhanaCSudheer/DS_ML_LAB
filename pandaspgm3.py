# write a python program using pandas and a) create a dataframe containing the names & marks of 3 students: Alice(79),Bob(92) & Charile(78).
# b) Display the entire dataset. c) Desplay the record of the student at index 0. d) Display only the students who scored more than 80 marks

import pandas as pd

# a) creating a dataframe
data = {"Name":["Alice","Bob","Charlie"],"Marks":[79,92,78]}
df = pd.DataFrame(data)

print("\nEntire dataset: ")
print(df)

print("\nRecord at index 0 is: ")
print(df.loc[0])       #  loc → selects using the index/label
print()
print("\nRecord at index 0 is: ")
print(df.iloc[0])     #  iloc → selects using the position number

print("\nStudents who scored more than 80: ")
print(df[df["Marks"] > 80])