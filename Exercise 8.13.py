# (Longest common prefix) Write a method that returns the longest common prefix
# of two strings. For example, the longest common prefix of distance and
# disinfection is dis. The header of the method is:
# def prefix(s1, s2)
# If the two strings have no common prefix, the method returns an empty string.
# Write a main method that prompts the user to enter two strings and displays their
# common prefix

def prefix(s1,s2):

    result = ""
    shortest = min(len(s1), len(s2))
    for i in range(shortest):
            if s1[i] == s2[i]:
                result += s1[i]
            else:
                break
    return result

def main():
    s1 = input("Enter the first String: ")
    s2 = input("Enter the second String: ")

    common = prefix(s1,s2)
    if common == "":
        print("The are no common prefixes for ", s1, "and", s2)

    else:
        print(f"The common prefix is {common}")

main()
