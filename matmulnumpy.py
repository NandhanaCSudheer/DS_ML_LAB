import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("The first array is: ")
print(arr1)
print()
print("The second array is: ")
print(arr2)
print()
print("Resultant matrix after dotmatrix multiplication is:")
print(np.dot(arr1,arr2))     # can apply only to square matrices
print(np.matmul(arr1,arr2))  
print()
print("Resultant matrix after matrix multiplication with its corresponding elements is:")
print(np.multiply(arr1,arr2))