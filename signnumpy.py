import numpy as np

arr = np.arange(16)
print(arr)
arr[9:16] = -arr[9:16]
print(arr)

# for i in range(9,16):
#     arr[i] = -i
# print(arr)
