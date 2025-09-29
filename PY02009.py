from collections import Counter

# đọc số bộ test
T = int(input())

for _ in range(T):
    # đọc số lần chọn ngẫu nhiên
    N = int(input())
    
    # đọc N số vào danh sách
    numbers = [int(input()) for _ in range(N)]
    
    # đếm tần suất
    freq = Counter(numbers)
    
    # tìm tần suất lớn nhất
    max_count = max(freq.values())
    
    # candidates = [num for num, count in freq.items() if count == max_count]
    

    candidates = []
    for num , count in freq.items():
        if count == max_count:
            candidates.append(num)
   


    print(min(candidates))
