def is_prime(n):
  if n  < 2 : return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def check(n):
  cnt_snt = 0
  cnt_conlai = 0
  if not is_prime(len(n)) : return False
  for i in n:
    if is_prime(int(i)):
      cnt_snt += 1
    else:
      cnt_conlai += 1
  if cnt_snt < cnt_conlai: return False
  
  return True

t = int(input())

for _ in range(t):
  n = input()
  if check(n):
    print("YES")
  else:
    print("NO")