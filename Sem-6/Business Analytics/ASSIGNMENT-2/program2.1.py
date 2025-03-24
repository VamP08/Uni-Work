import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Basic mathematical operations
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Reshape array
reshaped = arr.reshape(5, 1)
print("Reshaped Array:\n", reshaped)
