# Program to take a string input from the user and write it to a text file
text = input("Enter a string: ")
with open("output.txt", "w") as file:
    file.write(text)
print("The string has been written to output.txt")
