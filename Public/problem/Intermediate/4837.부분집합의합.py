T = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12]

n = 1 << len(arr)
blank = []
for i in range(n):
    blank1 = []
    for j in range(len(arr)):
        if i & (1 << j):
            blank1.append(arr[j])
    blank.append(blank1)

for t in range(1,T+1):
    data = list(map(int,input().split()))
    result = 0
    for i in range(len(blank)):
        total = 0
        if len(blank[i]) == data[0]:
            for j in range(len(blank[i])):
                total += blank[i][j]
        if total == data[1]:
            result += 1
    print(f'#{t} {result}')