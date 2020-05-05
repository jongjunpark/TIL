def tournament(x, y):
    if x == y:
        return x

    else:
        center = (x +y) // 2
        a = tournament(x, center)
        b = tournament(center + 1, y)

        if card[a] == card[b]:
            return a
        elif card[a] == 1:
            if card[b] == 2:
                return b
            else:
                return a
        elif card[a] == 2:
            if card[b] == 1:
                return a
            else:
                return b
        elif card[a] == 3:
            if card[b] == 1:
                return b
            else:
                return a

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    card = {num: cards[num] for num in range(len(cards))}

    result = tournament(0, N - 1)

    print("#{} {}".format(t, result+1))