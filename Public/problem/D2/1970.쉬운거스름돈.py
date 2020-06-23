T = int(input())
for t in range(1,T+1):
    money = int(input())
    arr = [0]*8
    if money//50000 != 0:
        arr[0] = money//50000
        money -= 50000*(money//50000)
    if money//10000 != 0:
        arr[1] = money//10000
        money -= 10000*(money//10000)
    if money//5000 != 0:
        arr[2] = money//5000
        money -= 5000*(money//5000)
    if money//1000 != 0:
        arr[3] = money//1000
        money -= 1000*(money//1000)
    if money//500 != 0:
        arr[4] = money//500
        money -= 500*(money//500)
    if money//100 != 0:
        arr[5] = money//100
        money -= 100*(money//100)
    if money//50 != 0:
        arr[6] = money//50
        money -= 50*(money//50)
    if money//10 != 0:
        arr[7] = money//10
        money -= 10*(money//10)
    result = ' '.join(map(str, arr))
    print(f'#{t}')
    print(f'{result}')