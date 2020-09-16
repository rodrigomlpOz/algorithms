def count_primes(n):
    primes = []
    primes = [False, False] + [True] * (n-1)
    for p in range(2, n):
        if primes[p]:
            primes.append(p)
            for j in range(p, n+1, p):
                primes[j] = False
    return primes





n = 15
count_primes(n)