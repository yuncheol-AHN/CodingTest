# 4344
# 평균은 넘겠지
# 2차원 배열 입력, int 포맷팅, average

'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''

N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
  arr[i] = list(map(int, input().split()))
  

for i in range(N):
  sum = 0
  for j in range(1, arr[i][0]+1):
    sum += arr[i][j]

  ave = sum/arr[i][0]

  answer = 0
  for j in range(1, arr[i][0]+1):
    if arr[i][j] > ave:
      answer += 1
  print('{:.3f}'.format(answer/arr[i][0]*100), '%', sep='')
