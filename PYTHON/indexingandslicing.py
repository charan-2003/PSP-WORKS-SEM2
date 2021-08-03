import numpy as np
arr = np.arange(10)
#prints array
print(arr)
#prints element of index 5
print(arr[5])
#prints elements from index 5 to 7
print(arr[5:8])
#changes the elements of index of 5,6,7 to 12
arr[5:8]=12
print(arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
#prints third element in first row
print(arr2d[0][2])
print(arr2d[0,2])

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0])
#arr3d[0] = 42
#print(arr3d)

print(arr3d[1,0])

print(arr2d)
print(arr2d[:2])
print(arr2d[:2,1:])
print(arr2d[1,:2])
print(arr2d[:,:1])