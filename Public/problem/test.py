def solution(N, stages):
    answer = [0] * N
    stage_num = [0]* (N+1)
    stage_not_clear = [0] * (N+1)
    for i in stages:
        stage_not_clear[i-1] += 1
        for j in range(i):
            stage_num[j] += 1
    fail_rate = []
    for k in range(N):
        tmp = stage_not_clear[k]/stage_num[k]
        fail_rate.append(tmp)
    for x in range(N):
        cnt = 0
        for y in range(N):
            if x<y:
                cnt += 1
        i = 0
        while True:
            if answer[cnt+i] == 0:
                answer[cnt+i] = (x+1)
                break
            else:
                i += 1
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N, stages)