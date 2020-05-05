T = int(input())
for t in range(1,T+1):
    st = input()
    binary = ''
    r_bi = []
    for i in st:
        zero = '0'*8
        if 'A'<=i<='Z':
            tmp = ord(i) - 65
        elif 'a'<=i<='z':
            tmp = ord(i) - 71
        elif '0'<=i<='9':
            tmp = ord(i) + 4
        elif i == '+':
            tmp = 62
        elif i == '/':
            tmp = 63
        a = str(bin(tmp))
        zero += a[2:]
        binary += zero[len(zero)-6::]
    for j in range(int(len(binary)/8)):
        blank = ''
        for i in range(8):
            blank += binary[8*j+i]
        r_bi.append(blank)
    result = ''
    for i in r_bi:
        a = int(i, 2)
        b = chr(a)
        result += b
    print(f'#{t} {result}')