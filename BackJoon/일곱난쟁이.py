# 일곱 난쟁이

from itertools import combinations

array = [int(input()) for _ in range(9)]

for e in combinations(array, 7):
  if sum(e) == 100:
    result = sorted(e)
    for item in result:
      print(item)
    break



array = [int(input()) for _ in range(9)]
array.sort()

for i in range(len(array) - 1):
  for j in range(i + 1, len(array)):
    if sum(array) - array[i] - array[j] == 100:
      for e in array:
        if e in [array[i], array[j]]:
          pass
        else:
          print(e)
      exit()

