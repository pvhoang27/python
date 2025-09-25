def is_prime(n):
  if n  < 2 : return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

t = int(input())

for _ in range(t): 
  n = input()
  dau = n[0] + n[1] + n[2]
  cuoi = n[-3] + n[-2] + n[-1]
  print(dau, cuoi)
  if is_prime(int(dau)) and is_prime(int(cuoi)):
    print("YES")
  else:
    print("NO")
