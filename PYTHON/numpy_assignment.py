#Creating an N-D array (By range):
import numpy as np
arr = np.arange(101)
arr_list = list(range(101))
print(arr)
print(arr_list)
print(type(arr))
print(type(arr_list))
arr2 = arr*2
print(arr2)

#N-D array (multidimensional)
import numpy as np
data = np.random.randn(2,3)
print(data)
print(type(data))
data1 = data*10
print(data1)
print(type(data1))
data2 = data+data
print(data2)
print(type(data2))
print(data.shape)
print(data.dtype)
#dtype? - data type

#Creating N-D arrays(By Array f/n):
data3 = [1,1.5,2,2.5,0]
arr3 = np.array(data3)
print(arr3)
print(type(arr3))

data4 = [[1,2,3,4],[5,6,7,8]]
arr4 = np.array(data4)
print(arr4)
print(type(arr4))
print(arr4.shape)
print(arr4.ndim)
print(arr4.dtype)

#zero arrays(1-d array):
arr5 = np.zeros(10)
print(arr5)
print(type(arr5))
print(arr5.shape)
print(arr5.ndim)
print(arr5.dtype)

#zero arrays(2-d array):
arr6 = np.zeros((3,6))
print(arr6)
print(type(arr6))
print(arr6.shape)
print(arr6.ndim)
print(arr6.dtype)

#zero arrays(3-d array):
arr7 = np.zeros((3,2,3))
print(arr7)
print(type(arr7))
print(arr7.shape)
print(arr7.ndim)
print(arr7.dtype)

#Datatypes for nd array:
arr8 = np.array([1,2,3], dtype = np.float64)
arr8.dtype
print(arr8)
print(type(arr8))
print(arr8.shape)
print(arr8.ndim)
print(arr8.dtype)

arr9 = np.array([11,12,13], dtype = np.int32)
arr9.dtype
print(arr9)
print(type(arr9))
print(arr9.shape)
print(arr9.ndim)
print(arr9.dtype)

arr10 = np.array([1, 2, 3, 4, 5])
arr.dtype
print(arr10.dtype)

arr_float = arr.astype(np.float64)
arr_float.dtype
print(arr_float.dtype)

#Cast to a floating point.
arr11 = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr11)
print(arr11.dtype)
arr12 = arr11.astype(np.int32)
print(arr12)
print(arr12.dtype)

#Array of strings.
num_str = np.array(['1.25','-9.6','42'], dtype = np.string_)
num_str.astype(float)
print(num_str)
print(type(num_str))
print(num_str.dtype)

int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
int_array.astype(calibers.dtype)
print(int_array)
print(calibers)

#Shortened type code strings:
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)
print(empty_uint32.dtype)

#Arithmetic with numpy arrays.
arr13 = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr13)
print(type(arr13))
print(arr13.shape)
print(arr13.ndim)
print(arr13.dtype)

#Arithmetic operations with it.
pro_arr13 = arr13 * arr13
print(pro_arr13)
print(type(pro_arr13))
print(pro_arr13.shape)
print(pro_arr13.ndim)
print(pro_arr13.dtype)

sub_arr13 = arr13 - arr13
print(sub_arr13)
print(type(sub_arr13))
print(sub_arr13.shape)
print(sub_arr13.ndim)
print(sub_arr13.dtype)

rec_arr13 = 1/arr13
print(rec_arr13)
print(type(rec_arr13))
print(rec_arr13.shape)
print(rec_arr13.ndim)
print(rec_arr13.dtype)

sqt_arr13 = arr ** 0.5
print(sqt_arr13)
print(type(sqt_arr13))
print(sqt_arr13.shape)
print(sqt_arr13.ndim)
print(sqt_arr13.dtype)

arr14 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(arr14)
print(arr13 > arr14)

#Basic indexing and slicing.
arr15 = np.arange(10)
print(arr15)
print(arr15[5])
print(arr15[4:7])
arr15[5:8] = 12
print(arr15)

#Slicing.
arr15_slice = arr15[5:8]
print(arr15_slice)

arr15_slice[1] = 12345
print(arr15_slice)
print(arr15)

#Bare slice[:].
arr15_slice[:] = 64
print(arr15_slice)
print(arr15)

#Higher dimensional arrays.
#2-d array.
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
print(arr2d[2])
print(arr2d[0][2])
print(arr2d[0, 2])

#3-d array.
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])

#Assign value in array.(We have used copy() option).
first_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
print(arr3d[0])

#Resigning the first values.
arr3d[0] = first_values
print(arr3d)
print(arr3d[0])
print(arr3d[1, 0, 1])

x = arr3d[1]
print(x)
print(x[0])

#Indexing with slicing.
#For 1-d array
print(arr15)
print(arr15[1:6])

#For 2-d array
print(arr2d)
print(arr2d[:2])

#Multiple slicing.
print(arr2d[:2, 1:])
print(arr2d[2, :1])
print(arr2d[2, 0:])
print(arr2d[:, :1])

arr2d[:2, 1:] = 0
print(arr2d)

#Boolean indexing.
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names)
print(names.dtype)
print(data)

print(names == 'Bob')
print(data[names == 'Bob'])
print(data[names == 'Bob', 2:])
print(data[names == 'Bob', 3])
print(names != 'Bob')
print(data[(names == 'Bob')])

cond = names == 'Bob'
print(data[cond])

mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])

data[data < 0] = 0
print(data)

data[names != 'Joe'] = 7
print(data)

#Fancy Indexing.
arr16 = np.empty((8, 4))
for i in range(8):
    arr16[i] = i
print(arr16)

print(arr16[[4, 3, 0, 6]])

print(arr16[[-3, -5, -7]])

#Reshaping an array.
arr17 = np.arange(32).reshape((8, 4))
print(arr17)
print(arr17[[1, 5, 7, 2], [0, 3, 1, 2]])

#Transposing arrays and swapping axes.
arr18 = np.arange(15).reshape((3, 5))
print(arr18)
#For transpose use 'T'.
print(arr18.T)

#Random array.
arr19 = np.random.randn(6, 3)
print(arr19)
print(np.dot(arr19.T, arr19))

#For High dimensional arrays.
arr20 = np.arange(16).reshape((2, 2, 4))
print(arr20)
print(arr20.transpose((1, 0, 2)))

#For swaping.
print(arr20.swapaxes(1, 2))

#Universal functions.
arr21 = np.arange(10)
print(arr21)
print(np.sqrt(arr21))
print(np.exp(arr21))
x = np.random.randn(8)
y =np.random.randn(8)
print(x)
print(y)

arr22 = np.random.randn(7) *5
print(arr22)

#Boolean arrays.
arr23 = np.random.randn(100)
print(arr23)
print(arr23>0)
print(arr23<0)
bools = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(bools.any())
print(bools.all())

#Mathematical methods.
arr24 = np.random.randn(5, 4)
print(arr24)
print(arr24.mean())
print(np.mean(arr24))
print(arr24.sum())
print(arr24.mean(axis=1))
print(arr24.sum(axis=0))

arr25 = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr25.cumsum())

#Sorting.
arr26 = np.random.randn(6)
print(arr26)
print(arr26.sort())
print(arr26)

arr27 = np.random.randn(5, 3)
print(arr27)
print(arr27.sort(1))
print(arr27)

#Linear algebra.
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print(y)
print(x.dot(y))
print(np.dot(x, y))
print(np.dot(x, np.ones(3)))

#Pseudo random number generation.
samples = np.random.normal(size=(4, 4))
print(samples)
print(np.random.seed(1234))
rng = np.random.RandomState(1234)
print(rng.randn(10))














