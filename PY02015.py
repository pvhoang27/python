def transform(A):
    return [
        abs(A[0] - A[1]),
        abs(A[1] - A[2]),
        abs(A[2] - A[3]),
        abs(A[3] - A[0])
    ]

while True:
    A = list(map(int, input().split()))
    if A == [0, 0, 0, 0]:
        break
    
    steps = 0
    while len(set(A)) != 1:   # chưa bằng nhau hết
        A = transform(A)
        steps += 1
    print(steps)
