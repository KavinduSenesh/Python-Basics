# pip install numpy - to install numpy
# pip3 install numpy - to install numpy for python3
# numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

import numpy as np

# Creating a numpy array
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

he = np.square(array_1)
print(he)
#square root of an array
sqr_array = np.sqrt(array_1)
print(sqr_array)

#sum of all elements in an array
result_sum = np.sum(array_1)
print(result_sum)

#subtraction of two arrays
result_sub = np.subtract(array_1, array_2)
print(result_sub)

#min and max of an array
min_array = np.min(array_1)
print(min_array)

max_array = np.max(array_1)
print(max_array)

#2D array
array_2D = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2D, type(array_2D))

#3D array
array_3D = np.array([[[1, 2, 3],[4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])
print(array_3D, type(array_3D))

#shape of an array - returns a tuple
print(array_1.shape)
print(array_2D.shape)
print(array_3D.shape)

#size of an array
print(array_1.size)
print(array_2D.size)
print(array_3D.size)

#ndim - minimum number of dimensions
print(array_3D.ndim)

#dtype - data type of an array
print(array_3D.dtype)

print(array_2D[0,0])
print(array_2D[1,2])

print(array_3D[1, 0 , 0])

# 1. create a 2D numpy array with the shape 4*5 containing the numbers 1 to 20 

# 2. perform the following operarion on the above matrix 
# add 10 to every element
# multiply every element by 2

# 3. claculate the square of each element 

# array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# print(array_2d)

# array_add10 = array_2d + 10
# print(array_add10)

# array_mult2 = array_2d * 2
# print(array_mult2)

# print(np.square(array_2d))


#check every element in the array and return True if the element is greater than 25
arr = np.array([10, 20, 30, 40, 50])
condition = arr > 25
print(condition)

#return the elements that satisfy the condition and store them in a new array
result_array = arr[condition]
print(result_array)

#one liner
filtered_array = arr[arr > 25]
print(filtered_array)

filtered_arrays = arr[(arr > 25) & (arr < 50)]
print(filtered_arrays)

# Q1. create a 1D array from 1 to 20.use boolean index into extract all even numbers
# Q2. given the numpy array with elements 10, 20 ,30, 40 and 50, use boolean indexing to extract all elements greater than the mean of the array

array_1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(array_1D[array_1D % 2 == 0])

array_Q2 = np.array([10, 20, 30, 40, 50])
print(array_Q2[array_Q2 > np.mean(array_Q2)])

#this will create an array of 5 elements with all elements as 0
print(np.zeros(5))
print(np.zeros((2, 3), dtype=int))
print(np.zeros((2, 3, 4)))

#this will create an array of 5 elements with all elements as 10
print(np.full(8, 10))
print(np.full((3, 4), 7))

print(np.empty((2, 3)))  