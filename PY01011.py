def is_thuan_nghich(num: str) -> bool:
    # Kiểm tra có phải số thuận nghịch và chỉ chứa 0,2,4,6,8
    return num == num[::-1] and all(ch in '02468' for ch in num) and len(num) % 2 == 1

t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    for i in range(22, n):  # Bắt đầu từ 22 vì đề cho N > 22
        if is_thuan_nghich(str(i)):
            result.append(str(i))
    print(" ".join(result))
