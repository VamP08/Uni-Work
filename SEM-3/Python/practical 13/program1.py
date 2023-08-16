import numpy as np

array1_1d = np.array([1, 2, 3, 4, 5])
array2_1d = np.array([6, 7, 8, 9, 10])
array1_2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
array2_2d = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])

sum_1d = array1_1d + array2_1d
sum_2d = array1_2d + array2_2d
print("Addition of 1-D Array =",sum_1d)
print("Addition of 2-D Array =",sum_2d)

sub_1d = array1_1d - array2_1d
sub_2d = array1_2d - array2_2d
print("Subtraction of 1-D Array =",sub_1d)
print("Subtraction of 2-D Array =",sub_2d)

mul_1d = array1_1d * array2_1d
mul_2d = array1_2d * array2_2d
print("Multiplication of 1-D Array =",mul_1d)
print("Multiplication of 2-D Array =",mul_2d)