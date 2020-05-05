def get_count(n):
    if n == N:
        return 1
    if n > N:
        return 0

    return get_count(n+10) + get_count(n+20)*2

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print("#%d"%t, get_count(0))