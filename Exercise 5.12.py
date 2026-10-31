# (Find numbers divisible by 5 and 6) Write a program that displays, ten numbers
# per line, all the numbers from 100 to 1,000 that are divisible by 5 and 6. The num-
# bers are separated by exactly one space.

count = 0
for i in range(100,1001):
    if i % 5 == 0 and i % 6 == 0:

            print(i, end =  " ")
            count += 1

            if count == 10:
                print()
                count = 0



