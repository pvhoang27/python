def sum_digits(n):
    s = 1
    while n > 0:
        s *= n % 10   # lấy chữ số cuối
        n //= 10      # bỏ chữ số cuối
    return s

def sort_key(x):
    return (sum_digits(x) ,x)

def sort_real(a):
    return sorted(a, key = sort_key)
    

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(sort_real(a))