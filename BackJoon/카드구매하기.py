# 카드 구매하기
# 최대 금액을 찾아라
# N
# 1 2 3 4 5 : N개
'''
N = int(input())
cards = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = cards[0]

for i in range(2, N+1):
  for j in range(i):
    dp[i] = max(dp[j] + cards[i-j-1], dp[i])

print(dp[N])
'''

# N
# 1 2 3 4 5 : N개

N = int(input())
cards = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = cards[1]

for i in range(2, N+1):
  for j in range(i):
    dp[i] = max(dp[j] + cards[i-j], dp[i])

print(dp[N])
