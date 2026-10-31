# (Sort three numbers) Write the following function to display three numbers in
# increasing order:
# def displaySortedNumbers(num1, num2, num3):
# Write a test program that prompts the user to enter three numbers and invokes the
# function to display them in increasing order. Here are some sample runs:

def displaySortedNumbers(num1,num2,num3):
    if num1 < num2 and num2 < num3:
        print(num1, num2, num3)

    elif num1 < num3 and num3 < num2:
        print(num1, num3, num2)

    elif num2 < num1 and num1 < num3:
        print(num2, num1, num3)

    elif num2 < num3 and num3 < num1:
        print(num2, num3, num1)

    elif num3 < num2 and num2 < num1:
        print(num3, num2, num1)

    elif num3 < num1 and num1 < num2:
        print(num3, num1, num2)

num1 = eval(input("Enter th 1st number: "))
num2 = eval(input("Enter the 2nd number: "))
num3 = eval(input("Enter the 3rd number: "))

displaySortedNumbers(num1,num2,num3)



