# https://projecteuler.net/problem=7

primes = []
n = 3
while 1:
    for j in range(2, n):
        if n % j != 0:
            continue
        else:
            break
    else:
        primes.append(n)
    if len(primes) == 10_000:
        print(max(primes))
        break
    n += 1