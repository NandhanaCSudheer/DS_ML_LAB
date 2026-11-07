# program to create a 2d array using numpy

import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
arr2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(arr2)
print()

m1 = np.add(arr1,arr2)
print("Added arrays: \n",m1)
print()
print(arr1 + arr2)
print()

print(f"difference = \n{np.subtract(arr1,arr2)}")
print(arr1 - arr2)
print()

print(f"Product = \n{np.multiply(arr1,arr2)}")
print("Matrix multiplication: ")
print(arr1 @ arr2)
print(np.matmul(arr1,arr2))
print()

print(f"Quotient = \n{np.divide(arr2,arr1)}")
print(arr2 / arr1)
print()

print(f"Quotient = \n{np.divmod(arr2,arr1)}")
print()

print("transpose of matrix 1 is: \n ",np.transpose(arr1))
print()

print("transpose of matrix 2 is: \n ",np.transpose(arr2))