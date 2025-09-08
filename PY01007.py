import math
t = int(input())

for _ in range(t):
    N, X, M = map(float, input().split())
    n = math.ceil(math.log(M / N) / math.log(1 + X / 100))
    print(n)
