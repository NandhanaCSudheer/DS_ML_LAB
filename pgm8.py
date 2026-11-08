import matplotlib.pyplot as plt
import pandas as pd

# lang = ["Java","Python","PHP","Javascript","C#","C++"]
# pop = [23,30,25,17,1,9]
# colors = ["red","blue","green","yellow","orange","pink"]
# plt.pie(pop,labels=lang,colors = colors,autopct="%1.1f%%")
# plt.show()

# data = pd.read_csv("pgm8.csv")
# count =  data["Country"]
# medal = data["Gold"]
# colors = ["red","blue","green","yellow","orange"]
# plt.pie(medal,labels=count,colors = colors,autopct="%1.1f%%")
# plt.show()

male = [55,56,74,23,35,48]
x = ["A","B","C","D","E","F"]
female = [78,67,54,36,54,58]

plt.subplot(2,2,1)
plt.bar(x,male,color = "red")
plt.xlabel("Name")
plt.title("Male")
plt.ylabel("Score")

plt.subplot(2,2,2)
plt.bar(x,female,color = "blue")
plt.xlabel("Name")
plt.title("Female")
plt.ylabel("Score")

plt.subplot(2,2,3)
plt.scatter(male,female,color = "red")
plt.title("Male vs female")

plt.subplot(2,2,4)
plt.plot(male,female,color = "red")
plt.title("Male vs female")
plt.xlabel("male")
plt.ylabel("female")

plt.show()