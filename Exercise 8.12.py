# (Bioinformatics: find genes) Biologists use a sequence of letters A, C, T, and G to
# model a genome. A gene is a substring of a genome that starts after a triplet ATG
# and ends before a triplet TAG, TAA, or TGA. Furthermore, the length of a gene
# string is a multiple of 3 and the gene does not contain any of the triplets ATG, TAG,
# TAA, and TGA. Write a program that prompts the user to enter a genome and displays
# all genes in the genome. If no gene is found in the input sequence, the program
# displays no gene is found. Here are the sample runs:


def findGenes():

    valid  = True

    genome = input("Enter a genome string: ")

    for char in genome:
        if char != "A" and  char != "C" and  char != "T"  and char != "G":
            valid = False




        found = False

    for i in range (len(genome) - 2):
        if genome[i:i + 3] == "ATG":

            for j in range(i + 3, len(genome) - 2, 3):
                three = genome[j:j + 3]
                if three == "ATG":
                    break

                if three == "TAG" or three == "TAA" or three == "TGA":
                    if j > i + 3:
                        print(genome[i + 3:j])
                        found = True
                    break

    if not found:
        print("no gene is found")
    else:
        print("Enter a valid input")

findGenes()








