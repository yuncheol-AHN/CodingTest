# 이친수
# n자리의 이친수의 개수를 찾아라
# 1 <= n <= 90

n = int(input())

dp_0 = [0] * (n+1)
dp_1 = [0] * (n+1)

dp_0[1] = 0
dp_1[1] = 1

for i in range(2, n+1):
  dp_0[i] = dp_0[i-1] + dp_1[i-1]
  dp_1[i] = dp_0[i-1]


print(dp_0[n] + dp_1[n])
