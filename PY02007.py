n  = 10
def chia(n):
  return n % 42

a = list(map(int, input().split()))
h = set()
for i in range(0,n):

  h.add(chia(a[i]))
print(len(h))