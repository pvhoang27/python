from itertools import combinations

n = 5
k = 3
arr = list(range(1, n+1))  # [1, 2, 3, 4, 5]

for comb in combinations(arr, k):
    print(comb)
