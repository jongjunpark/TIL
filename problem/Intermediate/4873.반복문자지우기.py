T = int(input())
for t in range(1, T+1):
    a = input()
    arr = []
    for i in a:
        arr.append(i)
    while True:
        count = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                del arr[i:i+2]
                break
        else:
            break
    print('#{} {}'.format(t,len(arr)))