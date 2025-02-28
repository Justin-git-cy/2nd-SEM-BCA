import numpy as np
arr = np.array([5, 2, 8, 1, 3])
arr2D = np.array([[3, 2, 1], [6, 5, 4]])

sorted_arr = np.sort(arr)
print(sorted_arr) 

sorted_desc = np.sort(arr)[::-1]
print(sorted_desc) 

sorted_rows = np.sort(arr2D, axis=0) 
print(sorted_rows)

sorted_cols = np.sort(arr2D, axis=1) 
print(sorted_cols)
