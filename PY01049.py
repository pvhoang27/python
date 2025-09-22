import math
def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0: return False
  
  return True

def check(n):
  cnt_prime = 0
  cnt_non_prime = 0
  for digit in n:
    if is_prime(int(digit)):
      cnt_prime += 1
    else :
      cnt_non_prime += 1
  return cnt_prime > cnt_non_prime
t = int(input())

for _ in range(t): 
  n = input()
  s = len(n)
  if check(n) and is_prime(s):
    print("YES")
  else:
    print("NO")
