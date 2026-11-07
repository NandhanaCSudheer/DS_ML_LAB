import matplotlib.pyplot as plt
import numpy as np

# Draw a line from position (1,3) and (2,10) then to (6,12) and finally to position (18,20). 
# Mark each point with a beautiful green color and set line colour to red and line style dotted. 


# x = np.array([1,2,6,18])
# y = np.array([3,10,12,20])
# plt.plot(x,y,marker = ".",mfc = "green",ms = 10,color = "red")
# plt.show()



# x = np.array([12,14,16,18,20,22,24])
# y = np.array([100,200,250,400,300,450,500])
# plt.xlabel("Temperature")
# plt.ylabel("Sales")
# plt.plot(x,y,marker = "*",mfc = "green",mec = "red",ms = 10,ls = "-")
# plt.show()


# python program to draw a line using given axis values taken from a text file,
#   with suitable labels in x and y axis and a title.


# file = open("pgm27plt.txt")
# x = np.array(list(map(int,file.readline().strip().split(" "))))
# y = np.array(list(map(int,file.readline().strip().split(" "))))
# file.close()
# plt.title("Temp Info")
# plt.xlabel("Count")
# plt.ylabel("Temperature")
# plt.plot(x,y,ls = "-",marker = "*",mfc = "black",mec = "black")
# plt.show()


# a python program to plot two or more lines on same plot with suitable legends for each line.

# x = np.array([1,2,3,4,5])
# y_1= np.array([30,32,31,32,33])
# y_2=np.array([27,26,29,28,29])
# plt.xlabel("Day")
# plt.plot(x,y_1,color="red",marker=".",mfc="red",label="Highest Temperature")
# plt.plot(x,y_2,color="blue",marker=".",mfc="blue",label="Lowest Temperature")
# plt.title("Temperature Difference")
# plt.legend() # adding legend to display labels
# plt.show()


# python program to create multiple plots.

# x = np.array([1, 2, 3, 4, 5])
# y_1 = np.array([30, 32, 31, 32, 33])
# y_2 = np.array([27, 26, 29, 28, 29])
# plt.figure(figsize=(10, 4)) 
# plt.subplot(1, 2, 1)
# plt.plot(x, y_1, color="red", marker=".", mfc="red", label="Highest Temperature")
# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("Highs")
# plt.subplot(1, 2, 2)
# plt.plot(x, y_2, color="blue", marker=".", mfc="blue", label="Lowest Temperature")
# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")
# plt.title("Lows")
# plt.suptitle("Temperature Difference Over 5 Days")
# plt.show()


# i.	Write a python program to display a bar chart of the popularity of programming languages.
# ii.	Write a python program to display a horizontal bar chart of the popularity of programming languages.
# (Make it red color).
# iii.	Write a python program to display a bar chart of the popularity of programming languages.
#  Use different colors for each bar.

# x_data = ["Java","Python","PHP","Javascript","C#","C++"]
# y_data=[22.2,17.6,8.8,8,77,6.7]
# plt.bar(x_data,y_data,color="blue")
# plt.show()

# plt.barh(x_data,y_data,color="red")
# plt.title("Programming Languages Popularity")
# plt.show()

# colors = ['red', 'green', 'blue', 'orange', 'purple']
# plt.bar(x_data,y_data,color=colors)
# plt.show()


# python program to create bar plots of scores by group and gender. Use multiple x values on the same chart for men and women.

# x_data = np.arange(1,6) *3
# y1= np.array([22,30,35,35,26])
# y2= np.array([25,22,30,35,29])
# bar_width=0.4
# plt.bar(x_data-bar_width,y1,label="Men",color='Blue')
# plt.bar(x_data+bar_width,y2,label="Women",color='Pink')
# plt.legend()
# plt.title("Scores by person")
# plt.show()


 # python program to create a pie chart on the popularity of programming languages.

# x_data = ["Java","Python","PHP","Javascript","C#","C++"]
# y_data=[30,40,10,10,5,5]
# plt.pie(y_data,labels=x_data)
# plt.show()


# python program to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.

# import pandas as pd
# df=pd.read_csv("medal.csv",delimiter=":")
# countries = df['Country'].to_numpy()
# medals=df['Gold_Medal'].to_numpy()
# plt.pie(medals,labels=countries,autopct='%1.1f%%')
# plt.pie(y_data,labels=x_data)
# plt.show()


# python Program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use marks of 10 students.

math_marks = np.array([88,92,80,89,100,80,60,100,80,34])
science_marks = np.array([35,79,79,48,100,88,32,45,20,30])
marks_range = np.array([10,20,30,40,50,60,70,80,90,100])
plt.xlabel("Marks Range")
plt.title("Math marks vs Science marks")
plt.scatter(marks_range,math_marks,color="red",label="Maths")
plt.scatter(marks_range,science_marks,color="green",label="Science")
plt.legend()
plt.show()