# numpy program to save given array to a text file and load it

import numpy as np

arr = np.arange(1,7,dtype = int)
np.savetxt("f13.txt",arr,fmt = "%d")  #  savetxt() -> used to store the array
str = np.loadtxt("f13.txt",dtype = int)   # loadtxt() -> for loading the array from the text file
print(str)