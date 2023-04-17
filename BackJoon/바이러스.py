# 2606
# 바이러스, BFS

# 노드 수, 간선 수
n = int(input())
m = int(input())

# graph
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# graph sort
for i in range(1, n+1):
  graph[i].sort()

visited = [False] * (n+1)
answer = 0

# bfs
def bfs():
  global answer
  visited[1] = True
  queue = [1]

  while queue:
    # print(queue, visited)
    v = queue.pop(0)
    answer += 1
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

bfs()
print(answer - 1)
