def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    for i in arr1:
        tmp = format(i, 'b')
        zero = '0'*(n - len(tmp))
        bin_tmp = zero + tmp
        bin_arr1.append(bin_tmp)
    for j in arr2:
        tmp = format(j, 'b')
        zero = '0'*(n - len(tmp))
        bin_tmp = zero + tmp
        bin_arr2.append(bin_tmp)
    for x in range(n):
        tmp = ''
        for y in range(n):
            if (int(bin_arr1[x][y]) + int(bin_arr2[x][y])) > 0:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer