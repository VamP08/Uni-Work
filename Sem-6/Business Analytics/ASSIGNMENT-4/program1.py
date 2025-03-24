import numpy as np

# Create a matrix
matrix1 = np.array([[1, 2], [3, 4]])

# Append a new row [7, 8]
matrix1 = np.vstack([matrix1, [7, 8]])

print("Updated Matrix:\n", matrix1)

# Create a sample array
arr8 = np.array([[10, 20, 30], [40, 50, 60]])

# Extract the second column
second_column = arr8[:, 1]

print("Second Column:", second_column)

# Find all elements in arr8 greater than 50
greater_than_50 = arr8[arr8 > 50]

print("Elements greater than 50:", greater_than_50)

# Replace all negative values in an array with zero
arr = np.array([-5, 10, -3, 8])
arr[arr < 0] = 0

print("Updated Array:", arr)

# Sort arr8 along columns
sorted_arr8 = np.sort(arr8, axis=0)

print("Sorted Array (Column-wise):\n", sorted_arr8)

# Multiply each element of arr8 by 2 without using a loop
arr8_multiplied = arr8 * 2

print("Array multiplied by 2:\n", arr8_multiplied)

# Subtract the mean of arr8 from each element
mean_subtracted = arr8 - np.mean(arr8)

print("Mean Subtracted Array:\n", mean_subtracted)

from numpy.linalg import det, eig

# Compute determinant of a matrix
matrix1 = np.array([[3, 4], [2, 1]])
determinant = det(matrix1)

print("Determinant of matrix1:", determinant)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(matrix1)

print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

from numpy.linalg import solve

# Solve system of equations:
# 3x + 4y = 10
# 2x + y = 5

A = np.array([[3, 4], [2, 1]])
b = np.array([10, 5])

solution = solve(A, b)

print("Solution for x and y:", solution)
