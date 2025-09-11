

t = int(input())
 
for _ in range(t):
  s = input()
  ok = 1
  for c  in s:
    if c not in '012' : 
      ok = 0
      break
    # else : ok = 0
  if ok == 1 :print("YES")
  else : print("NO")
