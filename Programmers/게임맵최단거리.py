# 최단거리 탐색
# queue
# 하나의 노드에서 모든 노드의 최단거리를 구할 수 있음

def solution(maps):
    answer = 0
    
    R, C = len(maps), len(maps[0])
    
    maps = [[float('inf') if maps[r][c] > 0 else 0 for c in range(C)] for r in range(R)]
    
    queue = [(0, 0, 1)] # row, col, val
    
    while queue: # queue가 빌 때까지 계속 실행
        cr, cc, cv = queue.pop(0)
        
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            if cr + dr in range(R) and cc + dc in range(C) and maps[cr + dr][cc + dc]:
                if cv + 1 < maps[cr + dr][cc + dc]:
                    maps[cr + dr][cc + dc] = cv + 1 # maps[r][c]의 값이 갱신됨
                    queue.append([cr + dr, cc + dc, cv + 1])
    
    if maps[R-1][C-1] == float('inf'):
        answer = -1
    else:
        answer = maps[R-1][C-1]
    
    return answer
