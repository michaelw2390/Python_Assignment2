# (Phone keypads) The international standard letter/number mapping for telephones is:
# Write a function that returns a number, given an uppercase letter, as follows:
# def getNumber(uppercaseLetter):
# Write a test program that prompts the user to enter a phone number as a string. The
# input number may contain letters. The program translates a letter (uppercase or
# lowercase) to a digit and leaves all other characters intact. Here is a sample run of
# the program:

def getNumber(uppercaseLetter):
     if  uppercaseLetter == "A" or uppercaseLetter == "B" or uppercaseLetter == "C":
         return 2
     elif uppercaseLetter == "D" or uppercaseLetter == "E" or uppercaseLetter == "F":
         return 3
     elif uppercaseLetter == "G" or uppercaseLetter == "H" or uppercaseLetter == "I":
         return 4
     elif uppercaseLetter == "J" or uppercaseLetter == "K" or uppercaseLetter == "L":
         return 5
     elif uppercaseLetter == "M" or uppercaseLetter == "N" or uppercaseLetter == "O":
         return 6
     elif uppercaseLetter == "P" or uppercaseLetter == "Q" or uppercaseLetter == "R" or uppercaseLetter == "S":
         return 7
     elif uppercaseLetter == "T" or uppercaseLetter == "U" or uppercaseLetter == "V":
         return 8
     else:
         return 9

def main():
    phoneNumber = input("Enter a string: ")
    result = ""
    for i in range(len(phoneNumber)):
        ch = phoneNumber[i]
        if ch.isdigit():
            result += ch
        elif ch.isalpha():
            result += str(getNumber(ch.upper()))
        else:
            result += ch
    print(result)
main()




