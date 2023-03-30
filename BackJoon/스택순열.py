# 1 2 3 4 5 6 7 8
# 4 3 6 8 7 5 2 1

# 1 6 2
# 1. pop 해야하는데 값이 더 큰 경우
import sys

n = int(input())

stk, result = [], []
arr = [n - i for i in range(n)]
flag = 0


while stk or arr:
  ipt = int(sys.stdin.readline())
  
  while True:
    if len(stk) == 0:
      stk = [arr.pop()]
      result.append('+')
    elif stk[-1] < ipt:
      stk.append(arr.pop())
      result.append('+')
    elif stk[-1] == ipt:
      stk.pop()
      result.append('-')
      break
    elif stk[-1] > ipt:
      flag = -1
      break
  
  if flag == -1:
    break
    
if flag == -1:
  print("NO")
else:
  for e in result:
    print(e)
