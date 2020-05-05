for tc in range(1,int(input())+1):
    string = input()
    s = list(string)
    H = int(input())
    location = list(map(int,input().split()))
    location.sort(reverse=True)
    for i in range(H):
        s.insert(location[i],'-')
    print('#{} {}'.format(tc,''.join(s)))