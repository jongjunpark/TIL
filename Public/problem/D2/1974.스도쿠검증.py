T = int(input())
for t in range(1, T + 1):
    board = []
    for i in range(9):
        num = list(map(int, input().split()))
        board.append(num)
    count = 0

    for i in range(9):
        for j in range(1, 10):
            if board[i].count(j) >= 2:
                count += 1
                break

    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(board[j][i])
        for k in range(1, 10):
            if tmp.count(k) >= 2:
                count += 1
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []
            for k in range(3):
                for l in range(3):
                    tmp.append(board[i + k][j + l])
            for k in range(1, 10):
                if tmp.count(k) >= 2:
                    count += 1
                    break
    if count == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')