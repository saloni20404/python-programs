# Program to read the content of a text file and print it to the console
with open("output.txt", "r") as file:
    content = file.read()
print(content)
