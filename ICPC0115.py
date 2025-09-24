t = int(input())

for _ in range(t):
  n = input()
   
  tong = 0
  
  for i in range(len(n)):
    h = int(n[i])
    tich = 1
    for num in range(1, h+1):
        tich *= num
    tong += tich
  # print(tich)
  # print(tong)
  if tong == int(n):
    print("Yes")
  else:
    print("No")

