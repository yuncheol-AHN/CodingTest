
# 2468, 안전영역
# BFS

n = int(input())
maps = []

for _ in range(n):
  l = list(map(int, input().split()))
  maps.append(l)

maxi = 0
mini = 101

for item in maps:
  maxi = max(maxi, max(item))
  mini = min(mini, min(item))


flood_maps = [] # 침수 유무 확인하기 위한 MAPS, 0, 1로 이루어짐
queue = []      # BFS를 위한 QUEUE
count = 0       # 침수 영역의 수를 위한 COUNT
result = 0      # 침수 영역의 최대값을 구하기 위한 RESULT

# hight : mini - maxi
for h in range(mini - 1, maxi+1):

  # maps
  for i in range(n):
    l = [0 if maps[i][j] <= h else 1 for j in range(n)]
    flood_maps.append(l)

  # area count
  for i in range(n):
    for j in range(n):
      
      # 침수 되지 않은 부분 발견
      if flood_maps[i][j] == 1:
        queue.append([i, j])

        while queue:
          cr, cc = queue.pop(0)
  
          for mr, mc in ((cr+1, cc), (cr, cc+1), (cr-1, cc), (cr, cc-1)):
            if 0 <= mr < n and 0 <= mc < n and flood_maps[mr][mc] != 0:
              queue.append([mr, mc])
              flood_maps[mr][mc] = 0
            
        count += 1
  
  flood_maps = []
  result = max(result, count)
  count = 0


print(result)
