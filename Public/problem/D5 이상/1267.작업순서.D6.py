T = 10
for t in range(1, T+1):
    v, e = map(int, input().split())
    number = list(map(int, input().split()))
    stack = []
    mat = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [0] * (v + 1)
    count = [0] * (v+1)

    for l in range(1,len(number),2):
        count[number[l]] += 1

    start = []
    start_count = 0
    for j in range(len(count)):
        if count[j] == 0:
            start_count += 1
            start.append(j)

    for k in range(0, len(number), 2):
        sta, end = number[k], number[k + 1]
        mat[sta][end] = 1

    result = []
    tmp = []
    for h in range(1, start_count):
        stack.append(start[h])
        while len(stack) > 0:
            current = stack[-1]
            if visited[current] == count[current] and current not in result:
                result.append(current)
            for i in range(len(mat[current])):
                if mat[current][i] == 1 and visited[i] < count[i] and (current,i) not in tmp:
                    visited[i] += 1
                    tmp.append((current,i))
                    if visited[i] == count[i]:
                        stack.append(i)
                        break
            else:
                stack.pop()

    ac = ' '.join(map(str,result))
    print('#{} {}'.format(t,ac))
