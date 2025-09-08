def is_non_decreasing(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

t = int(input().strip())  # số bộ test

for _ in range(t):
    s = input().strip()  # đọc số rất dài dưới dạng chuỗi
    print("YES" if is_non_decreasing(s) else "NO")
