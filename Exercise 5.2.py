# (Repeat additions) Listing 5.4, SubtractionQuizLoop.py, generates five random
# subtraction questions. Revise the program to generate ten random addition ques-
# tions for two integers between 1 and 15. Display the correct count and test time.

import random
import time
correctCount = 0
count = 0
NUMBER_OF_QUESTIONS = 10

startTime = time.time()

while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(0,15)
    number2 = random.randint(0,15)

    if number1 < number2:
        number1, number2 = number2, number1

    answer  = eval(input(" What is " + str(number1) + " - " + str(number2) + "? "))


    if number1 - number2 == answer:
        correctCount += 1
        print("Your are correct!")
    else:
        print("Your answer is wrong. \n", number1, "-", number2, "is", number1-number2)
    count += 1

endTime = time.time()
testTime = int(endTime - startTime)
print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")