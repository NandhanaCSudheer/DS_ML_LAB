import numpy as np

# arr = np.arange(30,61,2)
# print(arr)

# arr = np.array([100,98.4,91.50,99.78,101.5])
# cel = np.array([])
# for i in arr:
#     val = (i - 32) * (5 / 9)
#     cel = np.append(cel,val)
# print(cel)

# arr = np.array([32,40,180,360,45,93])
# rad = np.deg2rad(arr)
# print(rad)

# arr = np.array([1,2,3,4,5])
# print(arr.shape)
# r_arr = arr.reshape(1,-1)
# print(r_arr.shape)

# if np.any(arr == 6):
#     print("True")
# else:
#     print("False")

# if np.isin(6, arr):
#     print("True")
# else:
#     print("False")

# print(arr[arr == 7])
# print(arr[arr == 4])

# arr = np.diag([1,2,3,4])
# print(arr)

# arr = np.arange(1,21,dtype = int)
# arr[9:16] = -arr[9:16]
# print(arr)

# np.savetxt("pgm3.txt",arr,fmt = "%d")
# str = np.loadtxt("pgm3.txt",dtype = int)
# print(str)

# arr1 = np.array([1,2,3])
# arr2 = np.array([3,4,5,6,7])
# arr = np.concatenate((arr1,arr2))
# print(arr)
# print(np.split(arr,2))

arr = np.array([complex(1,2),complex(3,1),complex(2,7),complex(2,4),complex(2,5),complex(7,3),complex(5,4)])
sort = np.sort(arr)
print(arr)
print(sort)
print(sort[::-1])
