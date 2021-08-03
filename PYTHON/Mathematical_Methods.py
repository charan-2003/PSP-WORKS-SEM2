import numpy as np
arr = np.random.randn(5, 4)
print(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
print(arr.mean(axis=1))
print(arr.sum(axis=0))

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())