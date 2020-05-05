def white(x,s):
    if x == N-2:
        blue(x,s)
    else:
        white(x+1,s + color[x][1] + color[x][2])
        blue(x+1,s + color[x][1] + color[x][2])

def blue(x,s):
    if x == N-1:
        red(x,s)
    else:
        blue(x+1,s + color[x][0] + color[x][2])
        red(x+1,s + color[x][0] + color[x][2])

def red(x,s):
    global min_num
    if x == N:
        if s < min_num:
            min_num = s
        return
    else:
        red(x+1,s + color[x][0] + color[x][1])



for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    arr = [input() for _ in range(N)]
    color = []
    for i in range(N):
        color.append([arr[i].count('W'),arr[i].count('B'),arr[i].count('R')])
    min_num = 10000
    white(0, 0)
    print('#{} {}'.format(tc,min_num))
