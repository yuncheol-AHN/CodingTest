# 5014 스타트링크
# bfs

n, start, end, up, down = map(int, input().split())

visited = [False] * (n+1)
count = [0] * (n+1)

def bfs():
  queue = [start]

  while queue:
    
    # print(count, queue, visited)
    v = queue.pop()

    if v == end:
      break
    
    if not visited[v]:
      visited[v] = True
      
    for i in (v + up, v - down):
      if 0 < i <= n and not visited[i]:
        queue.append(i)
        count[i] = min(count[v] + 1, count[i]) if count[i] != 0 else count[v] + 1
        # print(queue, visited)


bfs()

if count[end] != 0:
  print(count[end])
else:
  if start != end:
    print('use the stairs')
  else:
    print(0)
