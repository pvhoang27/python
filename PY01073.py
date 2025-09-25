from itertools import permutations

# Đọc xâu ký tự S từ input
s = input()

# Sử dụng hàm permutations để tạo tất cả các hoán vị
# Vì xâu S ban đầu đã được sắp xếp, kết quả từ hàm permutations cũng sẽ theo thứ tự từ điển
all_permutations = permutations(s)

# Lặp qua từng hoán vị và in ra màn hình
for p in all_permutations:
    # Nối các ký tự trong mỗi hoán vị (là một tuple) lại thành một xâu
    print("".join(p))