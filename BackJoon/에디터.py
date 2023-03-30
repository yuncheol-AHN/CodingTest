# 스택, 큐를 파이프 형식으로 연결
# 시간 복잡도를 낮출 수 있다

import sys

str = input()
n = int(input())
idx = len(str)

left_stack = list(str)
right_stack = []

for _ in range(n):
  ipt = sys.stdin.readline().split()

  if ipt[0] == "L":
    if left_stack:
      right_stack.append(left_stack.pop())
  elif ipt[0] == "D":
    if right_stack:
      left_stack.append(right_stack.pop())
  elif ipt[0] == "B":
    if left_stack:
      left_stack.pop()
  elif ipt[0] == "P":
    left_stack.append(ipt[1])


left_stack.extend(right_stack[::-1])
print(''.join(left_stack))
