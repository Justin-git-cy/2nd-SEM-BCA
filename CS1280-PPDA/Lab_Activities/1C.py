def find_largest():
    print("Find the Largest Number")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    largest = max(num1, num2, num3)

    print("The largest number is:", largest)

find_largest()
