# 1.To write a Python program to represent student's marks using a bar graph. 
import matplotlib.pyplot as plt 
student = ["A", "B", "C", "D"] 
marks = [80, 75, 90, 85] 
plt.bar(student, marks) 
plt.title("Marks") 
plt.xlabel("Student") 
plt.ylabel("Marks") 
plt.show() 

# 2.To write a Python program to display data using a line graph. 
import matplotlib.pyplot as plt 
x = [1, 2, 3, 4, 5] 
y = [2, 4, 5, 4, 6] 
plt.plot(x, y) 
plt.title("Line Plot") 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.show() 

# 3.To write a Python program to represent the relationship between two variables using a scatter plot. 
import matplotlib.pyplot as plt 
x = [1, 2, 3, 4, 5] 
y = [2, 4, 5, 4, 6] 
plt.scatter(x, y) 
plt.title("Scatter Plot") 
plt.xlabel("X-axis") 
plt.ylabel("Y-axis") 
plt.show() 

# 4.To write a Python program to display the frequency distribution of student's marks using a histogram. 
import matplotlib.pyplot as plt 
marks = [45, 50, 60, 70, 80, 85, 90, 95] 
plt.hist(marks) 
plt.title("Histogram") 
plt.xlabel("Marks") 
plt.ylabel("Frequency") 
plt.show() 

# 5.To write a Python program to represent the percentage distribution of programming languages using a pie chart. 
import matplotlib.pyplot as plt 
labels = ["Python", "Java", "C"] 
sizes = [50, 30, 20] 
plt.pie(sizes,labels=labels,autopct="%1.1f%%") 
plt.title("Programming Languages") 
plt.show() 

# 6.To write a Python program to compare student's marks in Python and Java using a scatter plot. 
import matplotlib.pyplot as plt 
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
m = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34] 
s = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30] 
plt.scatter(x, m, label="Python Marks", marker="o") 
plt.scatter(x, s, label="Java Marks", marker="s") 
plt.xlabel("Test Number") 
plt.ylabel("Marks Scored") 
plt.title("Marks Range") 
plt.legend(loc="upper right") 
plt.grid(True) 
plt.show() 

# 7.To write a Python program to display data points connected by a dotted line using Matplotlib and NumPy. 
import matplotlib.pyplot as plt 
import numpy as np 
x_points = np.array([1, 2, 6, 18]) 
y_points = np.array([3, 10, 12, 20]) 
plt.plot( x_points, y_points,marker="o",color="red",linestyle="dotted") 
plt.show() 

# 8.To write a Python program to represent the popularity of different programming languages using a coloured bar graph. 
import matplotlib.pyplot as plt 
data = {"Java": 22.2,"Python": 17.6,"PHP": 8.8,"JavaScript": 8.0,"C#": 7.1,"C++": 6.7} 
courses = list(data.keys()) 
values = list(data.values()) 
colors = ["red", "yellow", "maroon","green", "black", "cyan"] 
plt.bar(courses, values, color=colors) 
plt.xlabel("Programming Language") 
plt.ylabel("Popularity") 
plt.title("Popularity of Programming Languages") 
plt.show() 

# 9. To write a Python program to Create Multiple Line Plots. 
import matplotlib.pyplot as plt 
x1 = [10, 20, 30] 
y1 = [10, 20, 30] 
x2 = [30, 40, 50] 
y2 = [30, 40, 50] 
plt.plot(x1, y1, label="Line 1") 
plt.plot(x2, y2, label="Line 2") 
plt.xlabel("X axis") 
plt.ylabel("Y axis") 
plt.title("Two Line Plot") 
plt.legend() 
plt.show() 

# 10. To write a Python program to  Bar Chart And A Horizontal Bar Chart Showing The Popularity Of Programming Languages. 
import matplotlib.pyplot as plt 
languages = ['Java', 'Python', 'PHP','JavaScript', 'C#', 'C++'] 
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7] 
plt.bar(languages, popularity) 
plt.xlabel("Programming Languages") 
plt.ylabel("Popularity") 
plt.title("Popularity of Programming Languages") 
plt.show() 
plt.barh(languages, popularity, color='red') 
plt.xlabel("Popularity") 
plt.ylabel("Programming Languages") 
plt.title("Popularity of Programming Languages") 
plt.show() 

# 11. Draw A Line Through The Points (1, 3), (2, 10), (6, 12) And (18, 20) Using Red Dotted Lines And Green Markers. 
import matplotlib.pyplot as plt 
x = [1, 2, 6, 18] 
y = [3, 10, 12, 20] 
plt.plot(x, y, marker='o', color='red', markerfacecolor='green', linestyle=':') 
plt.show() 