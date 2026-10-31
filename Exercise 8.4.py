# (Occurrences of a specified character) Write a function that finds the number of
# occurrences of a specified character in a string using the following header:
# def count(s, ch):


def count(s, ch):
    total = 0
    for  character in s:
        if character == ch:
            total += 1
    return total




s = input("Enter a string: ")
ch = input("Enter the character you want to count: ")

print(f"{ch} appears {count(s,ch)} times")

