import numpy as np
arr = np.array([1,2,3,4])
nums = np.array([[1,2,3],[4,5,6]])
a1 = np.arange(1,11)
a2 = np.arange(2,22,2)
print(arr)
print(nums)
print(nums.shape)
print(nums.ndim)
print(a1)
print(a2)
print(np.zeros(3))
print(np.ones(3))
print(np.zeros((3,3)))
print(np.zeros((3,3),dtype = int))
print(np.ones((3),dtype = int))

# write a numpy program to create an arry of all even numbers from 50 t0 90.

arr1 = np.arange(50,91,2)
print(arr1)

# import numpy as np

arr = np.array([1,2,3,4,5,6])
num = np.arange(6)
a1 = np.arange(1,7)

print(arr)
print(num)
print(a1)

print(arr.shape)
print(arr.ndim)

ra1 = arr.reshape(2,3)
print(type(ra1))

print(ra1.shape)
print(ra1.ndim)

a2 = np.array([10,20,30,40])
print(a2)
print(a2.shape)
print(type(a2))
rs2 = a2.reshape(4,1)
print(rs2)
print(rs2.shape)
print(type(rs2))

rs = a2.reshape(1,-1)
print(rs)
print(rs.shape)

a = np.array([10,20,30,40,50,60])
print(a)
print(a.shape)
an= np.arange(10,70,10)
print(an)
print(an.shape)
nan = an.reshape(1,-1)
print(nan)
print(nan.shape)