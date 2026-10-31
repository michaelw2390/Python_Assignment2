# (Use the isPrime Function) Listing 6.7, PrimeNumberFunction.py, provides the
# isPrime(number) function for testing whether a number is prime. Use this
# function to find the number of prime numbers less than 10,000.

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:

 # If true, number is not prime
            return False # number is not a prime
        divisor += 1

    return True # number is prime

def printPrimeNumbers(numberOfPrimes):
    NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
    count = 0 # Count the number of prime numbers
    number = 2 # A number to be tested for primeness
# Repeatedly find prime numbers
    while number < numberOfPrimes:
# Print the prime number and increase the count
        if isPrime(number):
            count += 1 # Increase the count

            print(number, end = " ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0: # Print the number and advance to the new line
                print()
 # Check if the next number is prime
        number += 1
    return count

def main():
    count = printPrimeNumbers(10000)
main()