import math

def prime_factors(n):
    factors = []
    
    # Loại bỏ các thừa số 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Kiểm tra các số lẻ từ 3 trở đi
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # Nếu n còn lại > 2 thì n là số nguyên tố
    if n > 2:
        factors.append(n)
    
    return factors

# Ví dụ sử dụng
n = int(input("Nhập số: "))
print("Các thừa số nguyên tố:", prime_factors(n))
