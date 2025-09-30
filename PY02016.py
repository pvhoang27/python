from collections import Counter

# Đọc số bộ test
T = int(input().strip())

for _ in range(T):
    # Đọc số phần tử
    N = int(input().strip())
    arr = list(map(int, input().split()))

    # Đếm tần suất xuất hiện của từng số
    freq = Counter(arr)

    # Tìm các số có số lần xuất hiện > N/2
    candidates = []
    for num, count in freq.items():
        if count > N // 2:
            candidates.append(num)

    # In kết quả
    if candidates:
        print(min(candidates))   # lấy số nhỏ nhất nếu có nhiều số thỏa mãn
    else:
        print("NO")
