import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9],dtype = int)

# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         arr[i] = 0

# print(arr)

arr[arr % 2 == 0] = 0
print(arr)