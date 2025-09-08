import math 
def is_prime(n):
  if n <= 2:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True
def sum_digits(n):
  return sum(int(digit) for digit in str(n))

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

t = int(input())

for i in range(t):
  a, b = map(int, input().split())
  ucln = gcd(a, b)
  sum_digits_ucln = sum_digits(ucln)
  if(is_prime(sum_digits_ucln)):
    print("YES")
  else:
    print("NO")
