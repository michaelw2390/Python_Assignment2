# (Format an integer) Write a function with the following header to format the integer
# with the specified width.
# def format(number, width):
# The function returns a string for the number with prefix 0s. The size of the string is
# the width. For example, format(34, 4) returns "0034" and format(34, 5)
# returns "00034". If the number is longer than the width, the function returns the
# string representation for the number. For example, format(34, 1) returns "34".
# Write a test program that prompts the user to enter a number and its width and displays
# a string returned from invoking format(number, width). Here is a sample run

def format(number, width):

    digit = 0
    temp = number
    if temp == 0:
        digit = 1
    while temp > 0:
        temp = temp // 10
        digit += 1

    result = str(number)
    for i in range(width - digit):
        result = "0" + result
    return result

def main():
    number = eval(input("Enter a number: "))
    width = eval(input("Enter the width: "))

    print("The formatted number is: ", format(number, width))

main()