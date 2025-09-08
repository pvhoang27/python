import math

# Hàm kiểm tra số nguyên tố
def is_prime(n) :
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Hàm đếm số nguyên tố cùng nhau với N
def count_coprimes(n: int) -> int:
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:  # Kiểm tra nguyên tố cùng nhau
            count += 1
    return count

# Xử lý input
t = int(input().strip())  # Số bộ test

for _ in range(t):
    n = int(input().strip())
    k = count_coprimes(n)
    print("YES" if is_prime(k) else "NO")
