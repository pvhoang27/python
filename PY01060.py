t = int(input())


for _ in range(t):  
  n =  input()
  sum = 0 
  tich = 1
  for digit in range(0, len(n)): 
    if digit % 2 == 0  : 
      if n[digit] != '0':
        tich *= int(n[digit])   
    else:
      sum += int(n[digit])
  print(str(tich) + " " + str(sum))
