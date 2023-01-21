# 1546
# 평균

N = int(input())
arr = list(map(int, input().split()))

answer = 0

newArr = [0] * N

for i in range(N):
  newArr[i] = arr[i]/max(arr)*100

answer = sum(newArr)/N

print(answer)
