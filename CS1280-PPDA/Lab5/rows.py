rows=int(input("Enter the number of rows : "))

for i in range(1,rows +1):
    print(" "*(rows-1) +" ".join(str(num) for num in range(1,i+1)))
