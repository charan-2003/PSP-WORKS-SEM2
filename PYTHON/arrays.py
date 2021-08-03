import numpy as np

data = np.random.rand(2,3)
#printing a 2X3 matrix
print(data)

#Arithmetic Operations
data = data*10
print(data)
data = data+data
print(data)

#Size of Matrix
size = data.shape
print(size)

#A data type is essentially an internal construct that a programming
# language uses to understand how to store and manipulate data.
typo = data.dtype
print(typo)


data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)

print(arr2.ndim)
print(arr2.shape)

print(arr1.dtype)
print(arr2.dtype)

print(np.zeros(3))
print(np.zeros((3,3)))

print(np.empty((3,3)))

print(np.arange(3))
print(list(range(3)))


