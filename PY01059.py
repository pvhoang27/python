t = int(input())


for _ in range(t):  
  n =  input()
  sum = 0 
  tich = 1
  for digit in range(0, len(n)): 
    if digit % 2 == 0: 
      sum += int(n[digit])
    else: 
      tich *= int(n[digit])
  print(str(sum) + " " + str(tich))