# (Display characters) Write a function that prints characters using the following
# header:
# def printChars(ch1, ch2, numberPerLine):
# This function prints the characters between ch1 and ch2 with the specified
# numbers per line. Write a test program that prints ten characters per line from 1
# to Z.


def printChars(ch1, ch2, numberPerLine):
    count = 0
    for i in range(ord(ch1),ord(ch2) + 1):
        print(chr(i), end=" ")
        count += 1


        if count % numberPerLine == 0:
            print("\n")




printChars("1","Z",10)