# def check(n):
   

t = int(input())  

for _ in range(t):
  n = input()
  s = n[::-1]
  # print(h)

  for i in range(1, len(n)):
     if abs(ord(n[i]) - ord(n[i - 1])) == abs(ord(s[i]) - ord(s[i - 1])):
       print("YES") 
       break
     else: 
      print("NO") 
      break 