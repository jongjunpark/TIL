for tc in range(1,int(input())+1):
    W, H, N = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        a = data[i][0] - data[i+1][0]
        b = data[i][1] - data[i+1][1]
        if a * b > 0:
           if min(abs(a),abs(b)) > 0:
               cnt += min(abs(a),abs(b))
               cnt += (max(abs(a),abs(b)) - min(abs(a),abs(b)))
        else:
            cnt += (abs(a) + abs(b))

    print('#{} {}'.format(tc,cnt))