# 2178, 미로 탐색
# bfs

from collections import deque

# 크기 입력
n, m = map(int, input().split())

# maps 변수
maps = []

# maps
for i in range(n):
  arr = list(map(int, input()))
  maps.append(arr)

for i in range(n):
  for j in range(m):
    if maps[i][j] == 1:
      maps[i][j] = 100001

maps[0][0] = 1

# visited
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True

# queue 생성
queue = deque([(0, 0, 1)])

# queue Loops
while queue:
  cr, cc, cv = queue.popleft()

  if cr == n-1 and cc == m-1:
    break

  for mr, mc in ((cr+1, cc), (cr, cc+1), (cr-1, cc), (cr, cc-1)):
    if 0 <= mr <= n-1 and 0 <= mc <= m-1 and maps[mr][mc] != 0 and not visited[mr][mc]:
      if maps[mr][mc] > cv:
        maps[mr][mc] = cv + 1
        queue.append([mr, mc, cv+1])
        visited[mr][mc] = True
  
print(maps[n-1][m-1])
