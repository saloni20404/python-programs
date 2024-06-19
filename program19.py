# Program to remove all punctuation from a given string
import string

text = input("Enter a string: ")
no_punctuation = text.translate(str.maketrans("", "", string.punctuation))
print("The string without punctuation is:", no_punctuation)
