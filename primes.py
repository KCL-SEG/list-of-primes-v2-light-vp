"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes < 1:
        raise ValueError
    else:
        list.append(2)
        x = 3
        while len(list) < number_of_primes:
            if isprime(x):
                list.append(x)
                x += 1
    return list

def isprime(number):
    for i in range(2, int(number/2)+1):
        if(number % i) == 0:
            return False
    else:
        return True
