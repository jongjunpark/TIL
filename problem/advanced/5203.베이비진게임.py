def baby_gin(card):
    runn(card)
    for k in range(6):
        triplet(card,card[k],k,1)
    return

def runn(card):
    global min_cnt
    for i in range(10):
        if card.count(i) >= 3:
            cnt = 0
            num = 0
            for j in range(6):
                if card[j] == i:
                    cnt += 1
                if cnt == 3:
                    num = j
                    break
            if num <= min_cnt:
                min_cnt = num
    return

def triplet(card,a,idx,cnt):
    global min_cnt
    if cnt == 3:
        if idx <= min_cnt:
            min_cnt = idx
        return

    for i in range(6):
        if card[i]+1 == a:
            if i >= idx:
                triplet(card,card[i],i,cnt+1)
            else:
                triplet(card,card[i],idx,cnt+1)
    else:
        return

for tc in range(1, int(input())+1):
    card = list(map(int,input().split()))
    player1 = card[0::2]
    player2 = card[1::2]
    print(player1)
    print(player2)
    result1 = 0
    result2 = 0
    min_cnt = 100
    baby_gin(player1)
    result1 = min_cnt
    min_cnt = 100
    baby_gin(player2)
    result2 = min_cnt
    print(result1,result2)
    if result1 < result2:
        print('#{} 1'.format(tc))
    elif result1 > result2:
        print('#{} 2'.format(tc))
    elif result1 == 100 and result2 ==100:
        print('#{} 0'.format(tc))
    else:
        print('#{} 1'.format(tc))