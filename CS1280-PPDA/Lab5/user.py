#Get user input
num =int(input("Enter a number: "))

#print the multipliation table
print(f"Multiplication Table of {num}:")
for i in range(1,11): #Loop from 1 to 10
   print(f"{num} x {i} ={num*i}")
