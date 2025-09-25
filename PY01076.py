def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)



t =int(input())

for _ in range(t):
    a = int(input())
    b = int(input())
    print(uscln(a, b))