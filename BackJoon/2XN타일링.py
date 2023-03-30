# Combinations

def comb(a, b):
  result = 1
  
  for i in range(a, a-b, -1):
    result *= i
  for j in range(b, 0, -1):
    result //= j

  return result

n = int(input())

if n%2 == 1:
  
  answer = 1
  for i in range((n+1)//2, n):
    answer += comb(i, n-i)
elif n%2 == 0:

  answer = 2
  for i in range(n//2 + 1, n):
    answer += comb(i, n-i)
    
print(answer%10007)

# DP - Top down

import sys
sys.setrecursionlimit(1000000)

n = int(input())
dict = {1:1, 2:2}

def tail(n):
  
  if n in dict.keys():
    return dict[n]

  result = tail(n-1) + tail(n-2)
  dict[n] = result
  return result

answer = tail(n) % 10007
print(answer)

# DP - Bottom up
