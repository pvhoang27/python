import math

def largest_prime_factor(n):
    max_prime = -1
    
    # Loại bỏ các thừa số 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    
    # Kiểm tra các số lẻ từ 3 trở đi
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    
    # Nếu n còn lại > 2 thì n là số nguyên tố
    if n > 2:
        max_prime = n
    
    return max_prime

# Ví dụ sử dụng
n = int(input("Nhập số: "))
print("Ước số nguyên tố lớn nhất:", largest_prime_factor(n))
