# def is_prime(num):
#   if num < 2:
#     return False
#   for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#       return False
#   return True
# def daoso(n):
#   return int(str(n)[::-1])
# t = int(input())  

# for _ in range(t):

#   n = int(input())  

#   for i in range(1, n + 1):
#     if is_prime(i) and is_prime(daoso(i))  and i != daoso(i) and daoso(i) <= n:
#       print(i, end = ' ')
#       print(daoso(i), end = ' ')
#   print()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def daoso(n):
    return int(str(n)[::-1])

t = int(input())

for _ in range(t):
    n = int(input())
    res = []
    for i in range(2, n):
        j = daoso(i)
        # chỉ in cặp (i, j) khi i < j để tránh trùng ngược lại
        if i < j and is_prime(i) and is_prime(j) and j < n:
            res.append((i, j))
    for a, b in res:
        print(a, b, end=" ")
    print()
