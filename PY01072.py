from itertools import combinations
# ham co san
# Đọc dữ liệu
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Lấy các phần tử khác nhau và sắp xếp
arr = sorted(set(arr))

# Sinh tổ hợp chập k
for comb in combinations(arr, k):
    print(" ".join(map(str, comb)))
