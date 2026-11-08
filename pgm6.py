import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x = [1,2,6,18]
# y = [3,10,12,20]
# plt.plot(x,y,marker = ".",mfc = "green",mec = "green",color = "red",ls = "dotted")
# plt.show()

# temp = [12,14,16,18,20,22,24]
# sales = [100,200,250,400,300,450,500]
# plt.plot(temp,sales,marker = "x",mec = "red",color = "blue")
# plt.xlabel("Temperature")
# plt.ylabel("Sales")
# plt.title("Temperature vs Sales")
# plt.show()

# x1 = [1,2,3,4]
# x2 = [4,5,6,7]
# y = [1,4,8,16]
# plt.plot(x1,y,label = "first",marker = "o")
# plt.plot(x2,y,label = "second",marker = "x")
# plt.legend()
# plt.show()

# m = [97,54,35,67,43,26,72,11,51,76]
# x = [1,2,3,4,5,6,7,8,9,10]
# s = [32,71,67,85,95,47,65,87,83,91]
# plt.scatter(x,m,color = "red",label = "Mathematics",cmap=".")
# plt.scatter(x,s,color = "blue" ,label = "Science",cmap = "x")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Mathematics vs Science")
# plt.legend()
# plt.show()

# data = pd.read_csv("pgm6.csv")
# x = data["X"]
# y = data["Y"]
# plt.plot(x,y,marker = ".",mec = "blue",color = "red")
# plt.show()

data = np.loadtxt("pgm6.txt",dtype = int)
x = data[:,0]
y = data[:,1]
plt.plot(x,y,marker = ".",mec = "blue",color = "red")
plt.show()