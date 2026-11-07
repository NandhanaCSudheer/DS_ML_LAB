import numpy as np  
a = np.array([[1, 2], [3, 4], [5, 6]]) 
U, S, VT = np.linalg.svd(a)  
print("Original matrix:\n", a)  
print("U matrix:\n", U)  
print("Singular values:\n", S)  
print("VT matrix:\n", VT) 