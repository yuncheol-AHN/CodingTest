# 요세푸스 순열
# N - K
# pop, remove, clear
# q.append(q.popleft())


from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
q = deque()
result = []

for i in range(1, n+1):
  q.append(i)

while q:
  for _ in range(k-1):
    q.append(q.popleft())
  result.append(q.popleft())

print(str(result).replace('[', '<').replace(']', '>'))
