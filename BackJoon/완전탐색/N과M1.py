
from itertools import permutations

N, M = map(int, input().split())

li = [str(i+1) for i in range(N)]

x = list(permutations(li, M))

for i in x:
    print(' '.join(i))
