n=int(input("Enter the number : "))
d=n-1
a=1
for i in range(n):
      print("  "*d,end=" ")
      for k in range(a):
           print("*",end="  ")
      print("\n")
      d=d-1
      a=a+2
