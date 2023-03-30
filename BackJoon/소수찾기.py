# 1978
# 소수 찾기
# range(2, int(math.sqrt(n)) + 1) -> % == 0 체크
import math

n = int(input())
l = map(int, input().split())
answer = 0
flag = 0

for num in l:
  if num == 1:
    continue
  elif num == 2:
    answer += 1
    continue
    
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0: # 소수 X
      flag = -1
      break

  if flag == 0:
    answer += 1
  else:
    flag = 0

print(answer)
