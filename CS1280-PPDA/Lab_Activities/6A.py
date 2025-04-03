import numpy as np

array = np.random.randint(1, 21, (3, 3))
print("Original Array:\n", array)

mean_value = np.mean(array)
print("\nMean of the array:", mean_value)

array[array < 10] = 0
print("\nModified Array:\n", array)
