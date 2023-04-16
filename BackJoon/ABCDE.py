# 13023

# 입력 값 받기
node, n = map(int, input().split())
graph = [[] for _ in range(node)]

# 방문 표시
visited = [False] * node

# 정답 변수 생성
answer = False

# 친구 관계 입력 받기
for _ in range(n):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# dfs
def dfs(idx, depth):
  
  global answer
  visited[idx] = True
  # print(idx, depth, visited)
  
  # 친구관계 4회 이상 연결
  if depth > 3:
    answer = True
    return

  # 친구관계 존재하는 지 확인
  for i in graph[idx]:
    if not visited[i]:
      dfs(i, depth + 1)
      visited[i] = False
      # print(idx, depth, visited)
          
# 0번부터 N-1번까지 확인
for i in range(node):
  dfs(i, 0)
  visited[i] = False

  if answer:
    break

# 정답 출력
if answer:
  print(1)
else:
  print(0)
