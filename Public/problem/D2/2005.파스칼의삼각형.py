T = int(input())
for t in range(1,T+1):
    inp = int(input())
    result = [[1], [1,1]]
    blank = []
    if inp == 1:
        print(f'#{t}')
        print(' '.join(map(str,result[0])))
    elif inp == 2:
        print(f'#{t}')
        print(' '.join(map(str,result[0])))
        print(' '.join(map(str,result[1])))
    else:
        for i in range(1,inp-1):
            blank.append(1)
            for j in range(i):
                blank.append(result[i][j] + result[i][j+1])
            blank.append(1)
            result.append(blank)
            blank = []
        print(f'#{t}')
        for i in range(inp):
            print(' '.join(map(str,result[i])))