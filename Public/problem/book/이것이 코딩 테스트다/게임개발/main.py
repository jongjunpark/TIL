# 첫 줄 : 맵 세로 크기 N, 맵 가로 크기 M
# 둘째 줄 : 캐릭터 좌표 A, B 바라보는 방향 d (0:북, 1:동, 2:남, 3:서)
# 셋째 줄부터 : 맵 정보 (외곽은 오로지 바다) (0: 육지, 1: 바다)
# 3 <= N, M <= 50
import sys
sys.stdin=open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
  N, M = map(int, input().split())
  A, B, d = map(int, input().split())

  game_map = [list(map(int, input().split())) for _ in range(N)]
  visited = [[0] * M for _ in range(N)]
  visited[A][B] = 1

  # d 에 따라 이동하게 될 delta값
  delta = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}

  # d 에 따라 뒤로 가는 delta값
  delta_back = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}

  # 회전한 횟수
  turn_cnt = 0

  while True:
    dx, dy = delta[d]
    x = A + dx
    y = B + dy

    if 0 <= x < N and 0 <= y < M:
      if game_map[x][y] == 0 and visited[x][y] == 0:
        d = (d-1) % 3
        A, B = x, y
        visited[A][B] = 1
      else:
        if turn_cnt == 4:
          dx, dy = delta_back[d]
          A += dx
          B += dy
          if game_map[A][B] == 1:
            break
          else:
            turn_cnt = 0
        else:
          turn_cnt += 1
          d = (d-1) % 4
  
  result = 0
  for i in visited:
    for j in i:
      if j == 1:
        result += 1
  
  print(result)