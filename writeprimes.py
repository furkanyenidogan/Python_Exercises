
import math as m

def writeprimes(n):
    def is_prime(s):
        if s % 2 == 0:
            return s == 2
        for i in range(3, int(m.sqrt(s)) + 1, 2):
            if s % i == 0:
                return False
        return True
    primes = []
    for i in range(2,n+1):
        if is_prime(i):
            primes.append(i)
    return print(primes)

writeprimes(100)
