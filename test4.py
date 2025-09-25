# import math

# def factorize(n):
#     sum = 0
#     i = 2
#     while i <= math.isqrt(n): 
#          # math.isqrt(n) = căn bậc 2 nguyên
#         while n % i == 0:
            
#             print(i, end=" ")
            
#             n //= i
#         i += 1
#     if n > 1:
#         print(n, end="")
        
#     print()
#     # print("Sum =", sum)

# # Ví dụ chạy
# factorize(60)


import math

def factorize(n):
    sum_factors = 0  # đổi tên biến để tránh trùng với hàm sum()
    i = 2
    while i <= math.isqrt(n):
        while n % i == 0:
            print(i, end=" ")
            sum_factors += i   # cộng vào tổng
            n //= i
        i += 1
    if n > 1:
        print(n, end=" ")
        sum_factors += n
    print()
    print("Sum =", sum_factors)

# Ví dụ chạy
factorize(60)
