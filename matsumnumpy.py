import numpy as np

arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])

col = np.sum(arr,axis=0)
row = np.sum(arr,axis = 1)
print("Sum: ",np.sum(arr))
print("Column sum: ",col)
print("Row sum: ",row)