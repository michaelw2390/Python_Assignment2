# (Reverse a string) Write a function that reverses a string. The header of the function
# is:
# def reverse(s):
# Write a test program that prompts the user to enter a string, invokes the reverse
# function, and displays the reversed string.

def reverse(s):
    return s[::-1]


rString = input("Enter a String: ")

reverse(rString)
print(reverse(rString))