t = int(input())

for _ in range(t):
  n = input().strip()

  is_lucky = True
  for digit in str(n):
    if digit not in ('4', '7'):
      is_lucky = False
      break

  print("YES" if is_lucky else "NO")
