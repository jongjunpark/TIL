def binary_search(start, end, target, lc, rc):
    global cnt
    if lc == 2 or rc == 2:
        return
    if start > end:
        return
    else:
        mid = (start+end)//2
        if A[mid] == target:
            cnt += 1
            return
        elif A[mid] > target:
            return binary_search(start, mid-1, target, lc+1, 0)
        else:
            return binary_search(mid+1, end, target, 0, rc+1)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    A = sorted(a)
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        binary_search(0, N-1, i, 0, 0)
    print('#{} {}'.format(tc,cnt))