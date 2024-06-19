# Program to count the occurrences of a specific element in a list
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print(f"The element {element} occurs {count} times in the list.")
