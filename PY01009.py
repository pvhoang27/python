
s = input()
lower = 0
upper = 0
for c in s:
    if c >= 'a' and c <= 'z':
        lower += 1
    elif c >= 'A' and c <= 'Z':
        upper += 1

if lower > upper:
    print(s.lower())
else:
    print(s.upper())
