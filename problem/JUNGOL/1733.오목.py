arr = []
for i in range(19):
    tmp = list(map(int,input().split()))
    arr.append(tmp)
delta = [(1,0),(0,1),(1,1),(-1,1)] #하 우 좌하 우하
result = [100,100,0]
asda = 0
for i in range(19):
    for j in range(19):
        if arr[i][j] == 1 or arr[i][j] == 2:
            k = 0
            count = 0
            a,b = i,j
            total = 0
            while k < 4:
                dx,dy = delta[k]
                X = i + dx
                Y = j + dy
                if 0 <= a - dx <= 18 and 0 <= b - dy <= 18:
                    if arr[a][b] == arr[a-dx][b-dy]:
                        k += 1
                        continue
                if X < 0 or X >= 19 or Y < 0 or Y >= 19:
                    if count == 4:
                        total += 1
                        count = 0
                        k += 1
                        i,j = a,b
                        asda += 1
                        continue
                    else:
                        count = 0
                        k += 1
                        i,j = a,b
                        continue
                else:
                    if arr[X][Y] == arr[i][j]:
                        count += 1
                        i,j = X,Y
                    else:
                        if count == 4:
                            total += 1
                            count = 0
                            k += 1
                            i,j = a,b
                            asda += 1
                        else:
                            count = 0
                            k += 1
                            i,j = a,b
            if total == 1:
                if b < result[1]:
                    result[0],result[1],result[2] = a, b, arr[a][b]
if asda >= 1:
    print(result[2])
    print(result[0]+1, result[1]+1)
if asda == 0:
    print('0')