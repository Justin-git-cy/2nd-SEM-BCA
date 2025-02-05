def is_palindrome(string):
   left, right = 0, len(string) - 1
   while right >= left:
       if string[left] != string[right]:
            return False
       left += 1
       right -= 1
   return True

user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
