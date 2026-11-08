import numpy as np
import random

# arr = random.randint(1,20) # 1 to 20 both included
# print(arr)

# a = random.randrange(1,20)  # 20 excluded
# print(a)

# a1 = random.randrange(0,20,2)  # generated an even number 
# print(a1)

# nums = random.sample(range(1,101),5)   # unique numbers between 1 to 100
# print(nums)

# n = [random.randint(1,100) for i in range (5)]   # with duplicates within 1 to 101
# print(n)

# arr1 = random.sample(range(1,100),10)
# print(arr1)
# arr = np.array([15,60,75,12,32,58,93,17,45,38,67,92])
# print(arr[arr > 50])
# arr1 = [i for i in arr1 if i >= 50]
# print(arr1)



# arr = np.array([25,34,1,56,34,25,67,74,3,5,3,3,2,6,7,5,87,93,92])
# l = np.array([],dtype = int)
# for i in range(len(arr)):
#     if np.sum(arr == i) == 1:
#         l = np.append(l,arr[i])
# arr = np.unique(arr)
# print(arr)
# print(np.sort(arr))
# print(l)


# arr = np.array([91,2,3,4,5,6,7,25,34,56,67,74,87,92,93])
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))
# print(np.var(arr))
# print(arr.T)
# print(np.transpose(arr))
# print(np.diff(arr))
# print(np.sum(arr))

# arr[arr%2 == 0] = 0
# print(arr)



arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
U,S,VT = np.linalg.svd(arr)
print(U)
print(S)
print(VT)

cols = np.sum(arr,axis = 0)
rows = np.sum(arr,axis = 1)
print(np.sum(arr))
print(cols)
print(rows)