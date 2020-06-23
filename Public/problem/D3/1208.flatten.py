for t in range(1, 11):
    dump = list(map(int, input().split()))
    block = list(map(int, input().split()))

    for j in range(dump[0] + 1):
        max_data = 0
        min_data = 100
        max_count = 0
        min_count = 0
        for idx, i in enumerate(block):
            if i >= max_data:
                max_data = i
                max_count = idx
        for idx, k in enumerate(block):
            if k <= min_data:
                min_data = k
                min_count = idx
        block[max_count] = max_data - 1
        block[min_count] = min_data + 1
        if (max_data - 1) - (min_data + 1) <= 1:
            print((max_data) - (min_data))
            break
    print("#{0} {1}".format(t, (max_data - min_data)))