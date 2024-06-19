# Program to check if a substring is present in a given string
string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in string:
    print("The substring is present in the main string.")
else:
    print("The substring is not present in the main string.")
