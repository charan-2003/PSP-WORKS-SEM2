import numpy as np

arr = np.random.randn(6)
print(arr)
print(arr.sort())
print(arr)

arr = np.random.randn(5, 3)
print(arr)
print(arr.sort(1))
print(arr)