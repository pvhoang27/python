# t = int(input())

# # hàm số thuận nghịch
# def is_palindrome(n): 
#     s = str(n)
#     return s == s[::-1]

# # hàm các chữ số chẵn
# def even_digit(n):
#     for ch in n :
#       if int(ch) % 2 == 1 : 
#          return 0
#     return 1

# def even_length(n):
#    if len(str(n)) % 2 == 1 : return  0
#    return 1

# for _ in range(t):
#   n = int(input())
#   # if even_digit(n) and even_length(n) :
#   for i in (22, n) :
#      if is_palindrome(i) and even_digit(str(i)) and even_length(i): 
#         print(i , end =' ')
#   print()


t = int(input())

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def even_digit(n):
    for ch in str(n):
        if int(ch) % 2 == 1:
            return 0
    return 1

def even_length(n):
    return 0 if len(str(n)) % 2 == 1 else 1

for _ in range(t):
    N = int(input())
    for i in range(22, N):
        if is_palindrome(i) and even_digit(i) and even_length(i):
            print(i, end=" ")   # in cùng 1 dòng
    print()  # xuống dòng sau mỗi test case
