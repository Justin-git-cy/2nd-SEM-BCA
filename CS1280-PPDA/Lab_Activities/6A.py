import numpy as np

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])  # 1D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

print("1D Array:\n", arr1)
print("2D Array:\n", arr2)

# Reshaping an array
reshaped_arr = arr1.reshape((5, 1))
print("Reshaped Array:\n", reshaped_arr)

# Basic array operations
arr3 = np.array([10, 20, 30, 40, 50])
sum_arr = arr1 + arr3  # Element-wise addition
print("Sum of Arrays:\n", sum_arr)

# Filtering elements
filtered_arr = arr1[arr1 > 2]  # Get elements greater than 2
print("Filtered Array:\n", filtered_arr)
