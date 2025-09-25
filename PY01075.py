import sys
import math

T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = {}  # dp[g] = chi phí nhỏ nhất để tạo ra GCD = g
    dp[0] = 0

    for ai, ci in zip(a, c):
        new_dp = dp.copy()
        for g, cost in dp.items():
            g_new = math.gcd(g, ai)
            cost_new = cost + ci
            if g_new not in new_dp or cost_new < new_dp[g_new]:
                new_dp[g_new] = cost_new
        dp = new_dp

    if 1 in dp:
        print(dp[1])
    else:
        print(-1)
