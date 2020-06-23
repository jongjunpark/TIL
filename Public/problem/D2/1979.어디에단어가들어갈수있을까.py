T = int(input())
for t in range(1,T+1):
    N,K = map(int, input().split())
    puzzle = []
    for i in range(N):
        num = list(map(int, input().split()))
        puzzle.append(num)
    w_count = 0
    h_count = 0
    result = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])-1):
            if w_count == K-1 and puzzle[i][j+1] == 0:
                result += 1
                w_count = 0
            if h_count == K-1 and puzzle[j+1][i] == 0:
                result += 1
                h_count = 0
            if (K-1 > w_count > 0 and puzzle[i][j+1] == 0) or (w_count > K-1 and puzzle[i][j+1] == 0):
                w_count = 0
            if (K-1 > h_count > 0 and puzzle[j+1][i] == 0) or (h_count > K-1 and puzzle[j+1][i] == 0):
                h_count = 0
            if puzzle[i][j] == 1 and puzzle[i][j+1] == 1:
                w_count += 1
            if puzzle[j][i] == 1 and puzzle[j+1][i] == 1:
                h_count += 1
        if w_count == K-1:
            result += 1
        if h_count == K-1:
            result += 1
        w_count, h_count = 0, 0
    print(f'#{t} {result}')