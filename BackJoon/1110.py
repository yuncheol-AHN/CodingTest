# 1110
# 더하기사이클
# 문제 정확하게 읽기

A = int(input())

answer = 1
sum = 0

def check(A):
  if A < 10:
    sum = A*11
  else:
    left = int(A/10)
    right = int(A%10)
    sum = right*10 + (left + right)%10
    
  return sum

sum = check(A)

while A != sum:
  sum = check(sum)
  
  answer += 1

print(answer)
