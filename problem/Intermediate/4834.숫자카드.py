T = int(input())
for t in range(1, T + 1):
    card = list(map(int, input().split()))
    number = ''.join(map(str, input().split()))
    numbers = []
    for i in number:
        numbers.append(int(i))

    blank = [0] * 10

    for i in range(len(numbers)):
        blank[9 - numbers[i]] += 1

    print("#{0} {1} {2}".format(t, (9 - blank.index(max(blank))), max(blank)))
