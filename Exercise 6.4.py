# (Display an integer reversed) Write the following function to display an integer in
# reverse order:
# def reverse(number):

def reverse(number):
    while number  > 0:

        digit = number % 10
        print(digit,end = " ",)
        number = number // 10




reverse(1234)


