import numpy as np
array = np.array([[1,2,3],[1,2,3]])
print(array)
print(array.shape)
print(type(array))
print(len(array))
print(array[0,1])
#It was hard one(my)
#print(array[0,[0,1,2]])
#This is the idiomatic one.(: indicates all).
print(array[0,:])
print(array[:,1])


