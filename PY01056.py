def is_prime(n):
    if n <= 1:
        return False  # Số không lớn hơn 1 không phải số nguyên tố

    #Sử dụng vòng lặp for để kiểm tra có tồn tại ước số nào khác lớn hơn 1 không
    for i in range(2, n):
        if n % i == 0: 
            return False  # Chỉ cần tìm thấy 1 ước số là biết không phải số nguyên tố

    return True  # Là số nguyên tố


def check(n):
    sum = 0 
    for i in n:
        sum += int(i)
    if not is_prime(sum) : return False


    for i in range(0, len(n)):
        if i % 2 == 0 and int(n[i]) % 2 != 0 : return False
        if i % 2 != 0 and int(n[i]) % 2 == 0 : return False
    return True


t = int(input())
for _ in range(t):  
    n = input()
    if check(n) : print("YES")
    else : print("NO")