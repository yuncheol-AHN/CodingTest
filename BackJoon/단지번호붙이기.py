
# maps 생성 & 구현
maps = []

for _ in range(n):
  arr = list(map(int, input()))
  maps.append(arr)

# queue, count, count_set, visited
queue = []
count = 0
count_set = []
visited = [[False for _ in range(n)] for _ in range(n)]

# count 생성
for i in range(n):
  for j in range(n):
    if maps[i][j] == 1 and visited[i][j] == False:
      maps[i][j] = 0
      count += 1
      visited[i][j] = True
      queue.append([i, j])
      
    while queue:
      r, c = queue.pop(0)
      for mr, mc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
        if 0 <= mr < n and 0 <= mc < n and maps[mr][mc] and not visited[mr][mc]:
          maps[mr][mc] = 0
          count += 1
          visited[mr][mc] = True
          queue.append([mr, mc])

    if count != 0:
      count_set.append(count)
      count = 0

count_set.sort()

print(len(count_set))
for c in count_set:
  print(c)
