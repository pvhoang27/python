def is_prime(n):
  if n < 2 : return False
  for i in range(2 , n):
    if n % i == 0 : return False
  return True


n = int(input())
cnt = {}
a = list(map(int, input().split()))


for num in a :
  if is_prime(num):
    if num not in cnt :
      cnt[num] = 1
    else : 
      cnt[num] += 1

for num in cnt :
  print(num , cnt[num])



