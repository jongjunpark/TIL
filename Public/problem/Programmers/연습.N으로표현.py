def solution(N, number):
    # 초기 set init
    dp = [set() for _ in range(8)]
    
    # 초기값 설정     
    for i in range(len(dp)):
        dp[i].add(int(str(N)*(i+1)))
        
        
    for i in range(len(dp)):
        for j in range(i):
            for x in dp[j]:
                for y in dp[i-j-1]:
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y != 0:
                        dp[i].add(x//y)
        if number in dp[i]:
            return i + 1
    else:
        return -1