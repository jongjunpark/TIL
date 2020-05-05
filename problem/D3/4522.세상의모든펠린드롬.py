for tc in range(1,int(input())+1):
    word = input()
    word_list = list(word)
    for i in range(len(word)//2):
        if word_list[i] == '?' and word_list[-1-i] != '?':
            word_list[i] = word_list[-1-i]
        elif word_list[i] != '?' and word_list[-1-i] == '?':
            word_list[-1-i] = word_list[i]
    original = ''.join(word_list)
    for i in range(len(word) // 2):
        word_list[i], word_list[-1 - i] = word_list[-1 - i], word_list[i]
    result = ''.join(word_list)
    if original == result:
        print('#{} Exist'.format(tc))
    else:
        print('#{} Not exist'.format(tc))