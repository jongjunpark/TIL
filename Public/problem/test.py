import sys

sys.stdin = open('input.txt', 'r')

N = int(input())
signal = input()

S = [[0] * N for _ in range(N)]
t = -1

for i in range(N):
    for j in range(i,N):
        t += 1
        S[i][j] = signal[t]

# print(S)