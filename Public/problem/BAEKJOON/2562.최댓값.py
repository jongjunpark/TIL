N = 9
count = 0
max_num = 0
max_count = 0
for i in range(N):
    count += 1
    a = int(input())
    if a > max_num:
        max_num = a
        max_count = count
print(max_num)
print(max_count)
