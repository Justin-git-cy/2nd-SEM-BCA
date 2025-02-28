import numpy as np
arr = np.arange(10)
print("Original array:", arr) 
print("Element at index 5:", arr[5]) 
print("Slice from index 5 to 8:", arr[5:8]) 
arr[5:8] = 12
print("Modified array:", arr)

arr_2d = np.array([[1,2,3],[4,5,6]])
print("Original array:", arr_2d)
print("Original array:", arr_2d.ndim)
print("Element at index 0:", arr_2d[0])
print("Slice from index at 0 form 1 to 3:", arr_2d[0,1:3])
arr_2d[1, 1] = 12
print("Modified array:", arr_2d)

# Create a 2D array
arr = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])
print("Original Array:\n", arr)
# Slice the first row
row_slice = arr[0, :]
# Slice the second column
col_slice = arr[:, 1]
# Slice a submatrix (rows 1-2, columns 2-3)
submatrix = arr[1:3, 2:4]
print("\nFirst Row:", row_slice)
print("Second Column:", col_slice)
print("Submatrix:\n", submatrix)
