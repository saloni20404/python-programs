# Program to convert a string into a list of its characters
def string_to_char_list(input_string):
    return list(input_string)
user_input = input("Enter a string: ")
char_list = string_to_char_list(user_input)
print("The list of characters is:", char_list)
