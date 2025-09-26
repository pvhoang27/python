def sieve_primes(n):
    """Trả về n số nguyên tố đầu tiên"""
    primes = []
    num = 2
    while len(primes) < n:
        ok = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                ok = False
                break
        if ok:
            primes.append(num)
        num += 1
    return primes

# Đọc input
N, X = map(int, input().split())

# Lấy N số nguyên tố đầu tiên
primes = sieve_primes(N)

# Tạo dãy kết quả
res = [X]
for p in primes:
    res.append(res[-1] + p)

# In ra kết quả
print(*res)
