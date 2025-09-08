t = int(input().strip())
for _ in range(t):
    n = input().strip()
    if n[:2] == n[-2:]:
        print("YES")
    else:
        print("NO")
