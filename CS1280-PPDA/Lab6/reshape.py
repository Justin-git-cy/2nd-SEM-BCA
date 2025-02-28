import numpy as np
arr = np.arange(24) 

reshaped_arr = arr.reshape(6, 4)
print("Original Array (1D):\n", arr)
print("Reshaped Array (3x4):\n", reshaped_arr)

reshaped_arr_3D = arr.reshape(2, 3, 4)
print("Reshaped Array (2x3x4):\n", reshaped_arr_3D)
