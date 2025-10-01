import sys
import math

MOD = 10**9 + 7

def prime_factors(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def solve(a, b):
    total_factors = {}
    for num in range(a, b+1):
        f = prime_factors(num)
        for p, e in f.items():
            total_factors[p] = total_factors.get(p, 0) + e
    
    res = 1
    for e in total_factors.values():
        res = (res * (2*e + 1)) % MOD
    return res

# ---- Main ----
t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(solve(a, b))
