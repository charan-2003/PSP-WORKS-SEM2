import numpy as np
"""
arr = np.array([1,2,3,4,5])
print(arr.dtype)

#converting to float
float_arr = arr.astype(np.float64)
print(float_arr.dtype)
"""
"""
arr = np.array([3.7,-1.2,2.6,0.5,12.9,10.1])
print(arr)
#conversion to int type
int_arr = arr.astype(np.int32)
print(int_arr)
#changing array to list
print(list(int_arr))
"""

numeric_strings = np.array(["1.25","-9.6","42"])
print(numeric_strings)
into_float = numeric_strings.astype(float)
print(into_float)
into_int = into_float.astype(int)
print(into_int)
print(list(into_int))

int_array = np.arange(10)
print(int_array)
calibers = np.array([.22,.270,.357,.380,.44,.50])
dtype = np.float64
print(int_array.astype(calibers.dtype))
