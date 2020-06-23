T = int(input())
for t in range(1,T+1):
    N = int(input())
    prob = []
    money = []
    for i in range(N):
        a, b = map(float,input().split())
        prob.append(a)
        money.append(b)
    result = 0
    for j in range(N):
        result += prob[j]*money[j]
    print('#{} {:0.6f}'.format(t,result))