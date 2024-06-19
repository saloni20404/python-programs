# Program to convert temperature from Celsius to Fahrenheit and vice versa
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ").upper()
temp = float(input("Enter the temperature: "))

if choice == 'C':
    print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit")
elif choice == 'F':
    print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius")
else:
    print("Invalid choice")
