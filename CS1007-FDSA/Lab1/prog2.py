arr = [12, 35, 1, 10, 34, 1, 45]

largest = second_largest = float('-inf')
smallest = second_smallest = float('inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second largest:", second_largest)
print("Second smallest:", second_smallest)
