# 1260

from collections import deque

def dfs(graph, i, visited):

  visited[i] = True
  print(i, end = ' ')
  
  for j in graph[i]:
    if not visited[j]:
      dfs(graph, j, visited)
  
  return

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n, l, s = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(l):
  a, b = map(int, input().split())

  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort()
  

visited = [False] * (n+1)

dfs(graph, s, visited)

print()
visited = [False] * (n+1)

bfs(graph, s, visited)
