a, K, N = map(int, input().split())

# Tìm số đầu tiên >= a+1 mà chia hết cho K
start = (a // K + 1) * K

if start > N:
    print(-1)
else:
    b = start - a           # b đầu tiên
    result = []
    while start <= N:       # tăng từng b theo bước K
        result.append(str(b))
        start += K
        b += K
    print(" ".join(result))
