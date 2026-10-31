# (Check SSN) Write a program that prompts the user to enter a Social Security
# number in the format ddd-dd-dddd, where d is a digit. The program displays
# Valid SSN for a correct Social Security number or Invalid SSN otherwise.

num = input("Enter the SSN: ")



while (len(num) != 11
       or num[3] != "-"
       or num[6] != "-"
       or not (num[0:3].isdigit() and num[4:6].isdigit() and num[7:11].isdigit())):
        print("Invalid Input")
        num = input("Enter the SSN: ")





print(num)
