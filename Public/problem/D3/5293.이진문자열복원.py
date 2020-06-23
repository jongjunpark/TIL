def check(a,b,c,d,s,k):
    global count
    if count > 0:
        return True
    if s == N:
        if a == 0 and b == 0 and c == 0 and d == 0:
            count += 1
            print('#{} {}'.format(t,k))
        return True
    if k[-1] == '0':
        if a > 0:
            return check(a-1,b,c,d,s+1,k+'0')
        if b > 0:
            return check(a,b-1,c,d,s+1,k+'1')
    elif k[-1] == '1':
        if d > 0:
            return check(a,b,c,d-1,s+1,k+'1')
        if c > 0:
            return check(a,b,c-1,d,s+1,k+'0')

T = int(input())
for t in range(1, T+1):
    q,w,e,r = map(int,input().split())
    N = q+w+e+r
    count = 0
    if check(q, w, e, r,0,'0'):
        continue
    if check(q, w, e, r,0,'1'):
        continue
    if count == 0:
        print('#{} impossible'.format(t))