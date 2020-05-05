T = int(input())
for t in range(1,T+1):
    # P = A사 요금/L,   Q = B사 기본요금    R = 기본요금 기준L  S = B사 요금/L (R이상 시)   W = 종민이가 쓰는 양
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W > R:
        B = Q + (W-R)*S
    else:
        B = Q
    if A > B:
        result = B
    else:
        result = A
    print(f'#{t} {result}')