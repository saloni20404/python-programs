# Program to calculate the sum of the digits of a given number
num = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in num)
print("The sum of the digits is:", sum_of_digits)
