def circle(num):
    global front
    front = (front + num) % len(cq)
    return print('#{} {}'.format(tc,cq[front]))


for tc in range(1,int(input())+1):
    N, M = map(int,input().split())
    cq = list(map(int,input().split()))
    front = 0
    circle(M)