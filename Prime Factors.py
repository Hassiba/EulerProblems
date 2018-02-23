# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from itertools import count, islice
from math import sqrt;

seed = int(input("Enter a number to factorize for primes: "))

factors = [1]


def isPrime(n):
    return (n > 1) and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def factorize(n):
    for i in islice(count(2), int(sqrt(n) - 1)):
        if isPrime(i) and n % i == 0:
            assert isinstance(i, int)
            factors.append(i)


factorize(seed)

print("All the factors of", seed, ":", factors)
print("The largest prime Factor is:", factors[-1])
