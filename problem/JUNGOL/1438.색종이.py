n = int(input())
arr = []
for i in range(100):
    tmp = [0]*100
    arr.append(tmp)
for k in range(n):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[x+i][y+j] = 1
result = 0
for i in range(100):
    result += arr[i].count(1)
print(result)