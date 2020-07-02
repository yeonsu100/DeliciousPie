import math

def primeFactors(n):
    # Print the number of two\'s that divide n
    while n % 2 == 0:
        print
        2,
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print
            i,
            n = n / i

    if n > 2:
        print
        n

n = 315
primeFactors(n)
