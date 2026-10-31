# (Display four patterns using loops) Use nested loops that display the following
# patterns in four separate programs:
# Pattern A Pattern B Pattern C Pattern D
# 1 1 2 3 4 5 6 1 1 2 3 4 5 6
# 1 2 1 2 3 4 5 2 1 1 2 3 4 5
# 1 2 3 1 2 3 4 3 2 1 1 2 3 4
# 1 2 3 4 1 2 3 4 3 2 1 1 2 3
# 1 2 3 4 5 1 2 5 4 3 2 1 1 2
# 1 2 3 4 5 6 1 6 5 4 3 2 1 1


# Pattern A
for i in range(1,7):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()

# Separates the Patterns
print()

#Pattern B
for i in range(6,0,-1):
    for j in range(1,i + 1):
        print(j, end= " ")
    print()

# Separator
print()

#Pattern C
for i in range(1,7):
    for j in range(6-i):
        print(" ", end= " ")
    for j in range(i, 0,-1):
        print(j, end= " ")
    print()

#Separator
print()

#Pattern D
for i in range(6,0,-1):
    for j in range(1,i - i):
        print(" ", end=" ")
    for j in range(1,i + 1):
        print(j, end= " ")
    print()












