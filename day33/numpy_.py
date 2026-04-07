# # numerical Python

# # library - dl , ml used

# # to do mathematical operations , linear algebra , fourier transform etc

# #  to get images , pixels

# # ipynb - interactive python notebook

# # GOOGLE COLAB

# # !pip list - to get the list of all the avaiable libraries

# # difference netween list and array

# #  list can store multiple data types values whereas array can store only inyeger , float or string 

# #  array is faster

# import numpy as np

# a = np.array([1,2,3,4,5])   # to create an array
# a

# a.ndim    # to get the dimension of the array

# print(type(a))  # to get the type

# # <class 'numpy.ndarray'>

# b = np.array([1,2,3,4,"hello"])   # all the values are converted to string
# b
# array(['1', '2', '3', '4', 'hello'], dtype='<U21')

# b.dtype


# c = np.array([1,2,4.5,6,7]) # here all are converted to float ----> int , float , string (order)
# c
# array([1. , 2. , 4.5, 6. , 7. ])


# b.size      # to get the no of elements
# 5

# # two dimensional array
# ab = np.array([[1,2],[2,3],[3,4]])
# ab

# array([[1, 2],
#        [2, 3],
#        [3, 4]])

# ab.shape  # (row,col) here 3 row and 2 col
# (3, 2)

# ab.ndim   # two dimension
# 2

# #index 0 1
# # 0    1 2
# # 1    2 3
# # 2    3 4

# # indexing starts from 0 both in row and col

# d = np.array([[1,2,3],[4,5,6],[7,8,9]])     # 3 rows and 3 cols
# d
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])


# #3D array
# three_d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# three_d

# array([[[1, 2],
#         [3, 4]],

#        [[5, 6],
#         [7, 8]]])

# three_d.shape   # (depth,row,col)   here depth is 2 , and in each depth the row and col is counted. so in first dept the no of rows is 2 and cols is 2
# (2, 2, 2)

# three_d.ndim
# 3

# three_d.size
# 8

# three_di = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]]) # the rows and cols in each depth should be the same
# three_di

# array([[[ 1,  2],
#         [ 3,  4]],

#        [[ 5,  6],
#         [ 7,  8]],

#        [[ 9, 10],
#         [11, 12]]])

# three_di.shape    # (depth,row,col)   here depth is 3 , and in each depth the row and col is counted. so in first dept the no of rows is 2 and cols is 2
# (3, 2, 2)

# three_di.size
# 12

# # 3D array with shape (2,3,3)
# ar = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
# ar
# array([[[ 1,  2,  3],
#         [ 4,  5,  6],
#         [ 7,  8,  9]],

#        [[10, 11, 12],
#         [13, 14, 15],
#         [16, 17, 18]]])


# ar.shape
# (2, 3, 3)

# # 2D with shape (2,4)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# arr
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])

# arr.shape
# (2,4)

# # numpy arrays are:
# # faster
# #  memory efficient
# # support mathematical operation directly

# # list ia a basic array

# # images are stored as arrays

# # feature       list           array

# # speed         slower         faster

# # data type     can store       usually same data type
#               # mixed datatypes

# # math operation  cannot directly   can directly

# # used in         general python   AI,ML,Data science


# # 1D
# # forward indexing
# # backward indexing
# y = np.array([1,2,3,4,5,6])
# y

# array([1, 2, 3, 4, 5, 6])

# y.shape
# (6,)

# y.ndim
# 1

# y[0]
# np.int64(1)

# print(y[0])   # forward indexing
# 1

# print(y[-1])    # backward indexing
# 6

# print(y[1:3])   # slicing
# [2 3]

# print(y[2:5])
# [3 4 5]

# # [5]
# print(y[-2])

# # [4,5,6]
# print(y[3:])

# # 2D
# h = np.array([[1,2,3],[4,5,6],[6,7,8]])
# h

# print(h[0])
# [1 2 3]

# print(h[0][0])
# 1

# print(h[1][1])
# 5

# print(h[2,1:])
# [7 8]

# print(h[3,0:2])
# [7 8]

# kl = np.arange(1,101,2)     #(start,stop,step)
# kl

# array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33,
#        35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67,
#        69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99])

#  print multiples of 3
# kp = np.arange(3,101,3)
# kp

# array([ 3,  6,  9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51,
#        54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99])

# reshape
# jk = np.array([[1,2,3,4],[4,5,6,7],[9,8,6,5]])
# jk

# array([[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [9, 8, 6, 5]])

# jk.reshape([4,3])
# array([[1, 2, 3],
#        [4, 4, 5],
#        [6, 7, 9],
#        [8, 6, 5]])

# jk.reshape([2,6])

# array([[1, 2, 3, 4, 4, 5],
#        [6, 7, 9, 8, 6, 5]])