import math

def factorize(n):
    sum_factors = 0  # đổi tên biến để tránh trùng với hàm sum()
    i = 2
    while i <= math.isqrt(n):
        while n % i == 0:
            # print(i, end=" ")
            sum_factors += i   # cộng vào tổng
            n //= i
        i += 1
    if n > 1:
        # print(n, end=" ")
        sum_factors += n
    return sum_factors

n = int(input())
a = []
sum = 0
for i in range(n):
  x = int(input())
  a.append(x)

for i in a : 
  sum += factorize(i)
print(sum)

