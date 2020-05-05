def min_cal(x):
    global max_num, min_num
    if x == N:
        if stack[-1] > max_num and cal.count(0) == 4:
            max_num = stack[-1]
        if stack[-1] < min_num and cal.count(0) == 4:
            min_num = stack[-1]
        return
    for i in range(4):
        if i == 0 and cal[i] > 0:
            cal[i] -= 1
            a = stack[-1] + num[x]
            stack.append(a)
            min_cal(x+1)
            cal[i] += 1
            stack.pop()
        elif i == 1 and cal[i] > 0:
            cal[i] -= 1
            a = stack[-1] - num[x]
            stack.append(a)
            min_cal(x+1)
            cal[i] += 1
            stack.pop()
        elif i == 2 and cal[i] > 0:
            cal[i] -= 1
            a = stack[-1] * num[x]
            stack.append(a)
            min_cal(x+1)
            cal[i] += 1
            stack.pop()
        elif i == 3 and cal[i] > 0:
            cal[i] -= 1
            a = int(stack[-1] / num[x])
            stack.append(a)
            min_cal(x+1)
            cal[i] += 1
            stack.pop()
    else:
        min_cal(x+1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cal = list(map(int,input().split()))
    num = list(map(int,input().split()))
    stack = []
    stack.append(num[0])
    min_num = 100000001
    max_num = -100000001
    min_cal(1)
    print('#{} {}'.format(t,max_num - min_num))