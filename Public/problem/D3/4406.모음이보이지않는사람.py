T = int(input())
vowel = ['a','e','i','o','u']

for tc in range(1,T+1):
    word = [x for x in input() if x not in vowel]
    print('#{} {}'.format(tc, ''.join(word)))