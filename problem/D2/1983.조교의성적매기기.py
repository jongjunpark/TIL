T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        score = list(map(int, input().split()))
        scores.append(score)
    totals = []
    total = 0
    for i in range(len(scores)):
        total += (scores[i][0]*0.35 + scores[i][1]*0.45 + scores[i][2]*0.2)
        totals.append(total)
        total = 0
    #K=2
    count = 1
    for i in totals:
        if i > totals[K-1]:
            count += 1
    if count <= N//10:
        print(f'#{t} A+')
    elif N//10 < count <= 2*N//10:
        print(f'#{t} A0')
    elif 2*N//10 < count <= 3*N//10:
        print(f'#{t} A-')
    elif 3*N//10 < count <= 4*N//10:
        print(f'#{t} B+')
    elif 4*N//10 < count <= 5*N//10:
        print(f'#{t} B0')
    elif 5*N//10 < count <= 6*N//10:
        print(f'#{t} B-')
    elif 6*N//10 < count <= 7*N//10:
        print(f'#{t} C+')
    elif 7*N//10 < count <= 8*N//10:
        print(f'#{t} C0')
    elif 8*N//10 < count <= 9*N//10:
        print(f'#{t} C-')
    else:
        print(f'#{t} D0')