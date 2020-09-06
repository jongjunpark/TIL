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
        if stage_num[k] == 0:
            tmp = 0
        else:
            tmp = stage_not_clear[k]/stage_num[k]
        fail_rate.append(tmp)
    for x in range(N):
        cnt = 0
        for y in range(N):
            if fail_rate[x]<fail_rate[y]:
                cnt += 1
        i = 0
        while True:
            if answer[cnt+i] == 0:
                answer[cnt+i] = (x+1)
                break
            else:
                i += 1
    return answer