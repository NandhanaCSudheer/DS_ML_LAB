import numpy as np

arr = np.array([4,3,6,5,8,4])

print("Mean of the array is ",np.mean(arr))
print("Maximum value of the array is ",np.max(arr))
print("Minimum value of the array is ",np.min(arr))
print("Standard Deviation of the array is ",np.std(arr))
print("Median of the array is ",np.median(arr))

arr = np.array([[12,24],[36,48]])
print(f"Minimum element = {np.min(arr)}\n Maximum element = {np.max(arr)}")
print(f"\n Trace = {np.trace(arr)}")