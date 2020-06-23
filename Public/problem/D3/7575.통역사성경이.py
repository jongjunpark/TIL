T = int(input())
for t in range(1, T+1):
    n = int(input())
    sentence = input()
    tmp = []
    data = []
    end = ['.','?','!']
    i = 0
    for j in range(n):
        blank = ''
        while True:
            blank += sentence[i]
            if sentence[i] in end:
                tmp.append(blank)
                break
            i += 1
        i += 1

    for i in range(len(tmp)):
        data.append(tmp[i].split())
    print('#{}'.format(t),end=' ')
    for i in range(len(data)):
        count = 0
        for j in range(len(data[i])):
            k = 1
            while True:
                if not 65 <= ord(data[i][j][0]) <= 90:
                    break
                elif k >= len(data[i][j]):
                    count += 1
                    break
                elif 97 <= ord(data[i][j][k]) <= 122 or ord(data[i][j][k]) == 32 or ord(data[i][j][k]) == 33 or ord(data[i][j][k]) == 46 or ord(data[i][j][k]) == 63:
                    k += 1
                else:
                    break
        print(count, end=' ')
    print()