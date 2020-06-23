T = int(input())
for t in range(1,T+1):
    n = int(input())
    scores = list(map(int, input().split()))
    max_count = 0
    score = 0
    for i in range(100):
        if i in scores:
            a = scores.count(i)
            if a >= max_count:
                max_count = a
                if i > score:
                    score = i
    print(f'#{t} {score}')