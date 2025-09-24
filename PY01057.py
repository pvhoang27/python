def is_prime(n):
  if n < 2 : return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0 : return False
  return True

def check(n):
  for i in range(0, len(n)):
    if is_prime(i):
      if not is_prime(int(n[i])):
        return False
  return True

t  = int(input())
for _ in range(t):
  n = input()
  if check(n) : print("YES")
  else : print("NO")