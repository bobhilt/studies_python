# Take user input, prints whether it's a palindrom

def is_palindrome(value):
    return value == value[::-1]
    
data = raw_input("Enter your phrase: ")

if is_palindrome(data):
    print(data + " is a palindrome.")
else:
    print(data + " is not a palindrome.")