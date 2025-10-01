

n, m = map(int, input().split())   # nhập số hàng và số cột
a = []

for i in range(n):
    row = list(map(int, input().split()))  # nhập 1 hàng
    a.append(row)

# In ra ma trận
for row in a:
    print(*row)
