# (Find the highest score) Write a program that prompts the user to enter the number
# of students and each student’s score, and displays the highest score. Assume that
# the input is stored in a file named score.txt, and the program obtains the input from
# the file.


num_of_students = eval(input("Enter the number of students: "))

highest_score = 0

for i in range(num_of_students):

    score = eval(input("Enter their score: "))

    if score > highest_score:
        highest_score = score

print(highest_score)











