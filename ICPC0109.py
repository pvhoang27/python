t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  sum = 0
  # for i in range(n):
  #   x = int(input())
  #   a.append(x)
  a.sort()
  sum = a[1] + a[2] + a[3]
  # sum = a[::-1] + a[::-2] + a[::-3]
  print(sum)

