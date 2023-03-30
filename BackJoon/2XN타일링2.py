
# 점화식 : f(n) = f(n-1) + 2*f(n-2)
# Top Down

import sys

sys.setrecursionlimit(100001)
n = int(input())

dict = {1:1, 2:3}

def recurs(n):
  if n in dict.keys():
    return dict[n]

  dict[n] = recurs(n-1) + 2*recurs(n-2)
  return dict[n]

print(recurs(n)%10007)

# Bottom Up

n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
  dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[n]%10007)
