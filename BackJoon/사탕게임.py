# 사탕 게임
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
# 최대 사탕 개수를 어떻게 확인 ? -> 바둑판에서 같은 요소의 길이 찾기

n = int(input())
array = []
result = 1

for _ in range(n):
  array.append(list(input()))

def check(array):
  answer = 1
  n = len(array)
  
  for i in range(n):
    
    cnt = 1
    for j in range(n-1):
      
      if array[i][j] == array[i][j+1]:
        cnt += 1
      else:
        cnt = 1
      answer = max(answer, cnt)
      
    cnt = 1
    for j in range(n-1):

      if array[j][i] == array[j+1][i]:
        cnt += 1
      else:
        cnt = 1
      answer = max(answer, cnt)
      
  return answer

for i in range(n):
  for j in range(n):
    
    if i+1 < n:
      
      array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
      result = max(result, check(array))
      array[i][j], array[i+1][j] = array[i+1][j], array[i][j]
    if j+1 < n:
      
      array[i][j], array[i][j+1] = array[i][j+1], array[i][j]
      result = max(result, check(array))
      array[i][j], array[i][j+1] = array[i][j+1], array[i][j]

print(result)
