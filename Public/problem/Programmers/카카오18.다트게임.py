def solution(dartResult):
    answer = 0
    num = ''
    result = []
    for i in dartResult:
        if 48 <= ord(i) <= 57:
            num += i
        elif i == 'S':
            result.append(int(num))
            num = ''
        elif i == 'D':
            result.append(int(num)**2)
            num = ''
        elif i == 'T':
            result.append(int(num)**3)
            num = ''
        elif i == '*':
            result[-1] *= 2
            if len(result) > 1:
                result[-2] *= 2
        else:
            result[-1] = -(result[-1])
    for j in result:
        answer += j
    return answer