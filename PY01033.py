from math import gcd

l, r = list(map(int, input().split()))

for i in range(l, r + 1):
  for j in range(i + 1, r + 1):
    for z in range(j + 1, r + 1):
      if gcd(i, j) == 1 and gcd(j, z) == 1 and gcd(z, i) == 1:
        print("(" + str(i) + ", " + str(j) + ", " + str(z) + ")")
        