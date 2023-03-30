# 쉬운 계단 수
# 예외 처리 - n = 1부터 하나하나 생각해보기

n = int(input())

stairs = [1 if i != 0 else 0 for i in range(10)]
  
for _ in range(n - 1):
  temp = stairs[:] # call by value
  for i in range(10):
    if i == 0:
      stairs[i] = temp[i+1]
    elif i == 9:
      stairs[i] = temp[i-1]
    else:
      stairs[i] = temp[i-1] + temp[i+1]

# print(stairs)
print(sum(stairs)%1000000000)
