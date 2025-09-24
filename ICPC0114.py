def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def check(n):
    # dieu kien 1 : n  la snt
    if not is_prime(int(n)):
        return False
    # dieu kien 2 : dao nguoc n la snt
    if not is_prime(int(n[::-1])): return False
    # dieu kien 3 : tong cac chu so  la snt
    sum = 0
    for digit in n:
        sum += int(digit)
    if not is_prime(sum):
      return False
    # dieu kien 4 : cac chu so cua n la snt
    for digit in n:
        if not is_prime(int(digit)):
            return False
        


    return True
t = int(input())

for _ in range(t):  

  n =  input()
  if check(n):
      print("Yes")
  else:
      print("No")
