T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())
    submit = list(map(int,input().split()))
    result = []
    for i in range(1,N+1):
        if i not in submit:
            result.append(i)
    print('#{} {}'.format(t,' '.join(map(str,result))))