import sys

n = int(sys.stdin.readline())

def prime_factors(n):
    factors = set()
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors

def euler_totient(n):
    if n == 1:
        return 1
    factors = prime_factors(n)
    result = n
    for factor in factors:
        result *= (1 - 1/factor)
    return int(result)

print(euler_totient(n))