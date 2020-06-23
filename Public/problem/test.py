import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    N = int(input())
    dirt = [list(map(int,input().split())) for _ in range(N)]
    

