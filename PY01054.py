t = int(input()) 

for _ in range(t):  
  n = input()
  tich  = 1
  for i in n :
    if i == '0' : i = '1'
    tich *= int(i)
  print(tich)