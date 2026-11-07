import numpy as np  

arr = np.arange(1, 13)  
print(np.shape(arr))
print(arr.reshape(3, 4))
print(np.shape(arr)) 
arr2 = np.array([1,2,3,4,5])
print(np.shape(arr2))
print(arr2.reshape(-1,1))
print(np.shape(arr2))