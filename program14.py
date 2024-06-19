# Program to read multiple lines of input from the user until they enter an empty line, then print all the lines
lines = []
print("Enter lines of text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("You entered:")
for line in lines:
    print(line)
