import numpy as np

arr = np.array([1,2,3,4,3,5,5,6,3,4,5,7,8])

print(np.unique(arr))

unique = np.array([], dtype=int)

for i in arr:
    if np.sum(arr == i) == 1:
        unique = np.append(unique, i)

print(unique)