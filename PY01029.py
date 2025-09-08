import math

t = int(input())

for _ in range(t): 
  n = int(input())

  reverse_n = str(n)[::-1]

  n_int = int(n)

  reverse_n_int = int(reverse_n)


  if math.gcd(n_int, reverse_n_int) == 1:
    print("YES")  
  else:
    print("NO") 

