def solve(arr, n):
    stack = []   # lưu chỉ số
    res = [0]*n

    for i in range(n):
        # bỏ các phần tử <= A[i] khỏi stack
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if not stack:  
            res[i] = i + 1   # không có phần tử lớn hơn bên trái
        else:
            res[i] = i - stack[-1]

        stack.append(i)

    return res


# ---- Main ----
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = solve(arr, n)
    print(*ans)
