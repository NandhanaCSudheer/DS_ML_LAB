# find determinant of a matrix

import numpy as np

arr = np.array([[5,1],[2,6]])

determinant = np.linalg.det(arr)
print(determinant)
print(round(determinant))
print(f"{determinant:.2f}")

inverse = np.linalg.inv(arr)
print(inverse)