import matplotlib.pyplot as plt
import pandas as pd

# lang = ["Java","Python","PHP","Javascript","C#","C++"]
# pop = [22.2,17.6,8.8,8.0,7.7,6.7]

# plt.bar(lang,pop,color = "blue")
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.show()

# plt.barh(lang,pop,color = "red")
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.show()

# colors = ["red","blue","green","yellow","orange","pink"]
# plt.bar(lang,pop,color = colors)
# plt.xlabel("Languages")
# plt.ylabel("Popularity")
# plt.show()

# data = pd.read_csv("pgm7.csv")
# x = data["Name"]
# y = data["Marks"]
# plt.bar(x,y,color = "blue")
# plt.xlabel("Name")
# plt.ylabel("Marks")
# plt.show()

# m = [97,54,35,67,43,26,72,11,51,76]
# x = [1,2,3,4,5,6,7,8,9,10]
# s = [32,71,67,85,95,47,65,87,83,91]
# plt.hist(m,bins = 5,color="skyblue", edgecolor="black")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.title("Distribution of Mathematics Marks")
# plt.show()

male = [55,56,74,23,35,48]
x = ["A","B","C","D","E","F"]
female = [78,67,54,36,54,58]

plt.subplot(1,2,1)
plt.bar(x,male,color = "red")
plt.xlabel("Name")
plt.title("Male")
plt.ylabel("Score")

plt.subplot(1,2,2)
plt.bar(x,female,color = "blue")
plt.xlabel("Name")
plt.title("Female")
plt.ylabel("Score")
plt.suptitle("Male vs Female Scores")
plt.show()