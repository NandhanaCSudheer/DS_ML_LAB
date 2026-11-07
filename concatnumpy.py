import numpy as np

arr1 = np.array([1,3,5])
arr2 = np.array([2,4,6])

print("First array: ",arr1)
print("Second array: ",arr2)
concat = np.concatenate((arr1,arr2))
print("Array after concatenation is: ",np.sort(concat))
print(np.concat((arr1,arr2)))