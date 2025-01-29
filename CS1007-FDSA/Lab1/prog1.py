arr = [11, 5, 16, 2, 43, 7, 21]

smallest = arr[0]
largest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print("Smallest element:", smallest)
print("Largest element:", largest)
