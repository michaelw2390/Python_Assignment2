# (Math: pentagonal numbers) A pentagonal number is defined as for n(3n-1)/2
#  for n = 1,2 and so on. So, the first few numbers are 1, 5, 12, 22, .... Write a
# function with the following header that returns a pentagonal number:

def getPentagonalNumbers(n):
    return (n * (3 * n - 1) //2)

for n in range(1,101):
    print(getPentagonalNumbers(n), end=" ")
    if n % 10 == 0:
        print()












