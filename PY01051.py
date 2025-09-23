
# for i in range(int(input())):
#     sum = 0
#     for i in input():
#         sum += int(i)

#     if str(sum) == str(sum)[::-1] and sum >  9:
#         print("YES")
#     else:
#         print("NO")


# # s  = input()
# # t =  str(s)[::-1]

# # print(t)


t = int(input())
for _ in range(t): 
  n =  input()
  sum = 0 
  for i in n : 
    sum += int(i)

  h = str(sum)
  if str(sum) == str(sum)[::-1] and len(h) > 1:
    print("YES")
  else:
    print("NO")

