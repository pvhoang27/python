def lam_tron_so(n: int) -> int:
    # Nếu n <= 10 thì giữ nguyên, không cần làm tròn
    if n <= 10:
        return n

    base = 10
    while n > base:
        n = ((n + base // 2) // base) * base
        base *= 10
    return n


# Đọc số lượng test
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(lam_tron_so(n))
