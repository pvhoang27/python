def is_prime(n):
    if n < 2 : return False

    for i in range(2 , n):
        if n % i == 0 : return False
    return True


n, m = map(int, input().split())   # nhập số hàng và số cột
a = []

for i in range(n):
    row = list(map(int, input().split()))  # nhập 1 hàng
    a.append(row)
    
for i in range(n):
    for j in range(m):
        if is_prime(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0

for row in a:
    print(*row)