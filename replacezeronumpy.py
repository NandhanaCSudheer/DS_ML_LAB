import numpy as np

arr = np.array([6,4,3,8,7,3,9,1,5],dtype = int)

# m = np.mean(arr)
# for i in range(len(arr)):
#     if arr[i] > m:
#         arr[i] = 0
# print(arr)

mean = np.mean(arr)  
arr[arr > mean] = 0  
print(arr) 