# f(n) = f(n-1) + f(n-2) + f(n-3)
# Bottom Up

num = int(input())
result = []

for _ in range(num):
  n = int(input())

  dp = [0] * (n+1)
  if n < 3:
    result.append(n)
    continue
  elif n == 3:
    result.append(4)
    continue
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4

  for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

  result.append(dp[n])

for e in result:
  print(e)

# Top down

num = int(input())
dict = {1:1, 2:2, 3:4}
result = []

def recurs(n):
  if n in dict.keys():
    return dict[n]

  dict[n] = recurs(n-1) + recurs(n-2) + recurs(n-3)
  return dict[n]

for _ in range(num):
  n = int(input())

  result.append(recurs(n))


for e in result:
  print(e)
