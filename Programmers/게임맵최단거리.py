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


from heapq import heappush, heappop

def solution(maps):
    # [y][x]
    answer = 0
    R, C = len(maps), len(maps[0])
    
    board = [[float('inf') if maps[r][c] == 1 else 0 for c in range(C)] for r in range(R)]
    
    QUEUE = [(1, 0, 0)]
    board[0][0] = 1
    
    while QUEUE:
        cv, cr, cc = heappop(QUEUE)
        
        # if cr == R-1 and cc == C-1:
        #     break
        
        # rd, cd를 통해서 코드의 길이를 줄일 수 있다
        for rd, cd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = cr + rd, cc + cd
            
            if nr in range(R) and nc in range(C) and board[nr][nc] != 0:
                if cv+1 < board[nr][nc]:
                    board[nr][nc] = cv+1
                    heappush(QUEUE, (cv+1, nr, nc))
        
        '''
        if cr+1 in range(R) and maps[cr+1][cc] != 0:
            if board[cr][cc] + 1 < board[cr+1][cc]:
                board[cr+1][cc] = board[cr][cc] + 1
                heappush(QUEUE, (cv+1, cr+1, cc))
        if cc+1 in range(C) and maps[cr][cc+1] != 0:
            if board[cr][cc] + 1 < board[cr][cc+1]:
                board[cr][cc+1] = board[cr][cc] + 1
                heappush(QUEUE, (cv+1, cr, cc+1))
        if cr-1 in range(R) and maps[cr-1][cc] != 0:
            if board[cr][cc] + 1 < board[cr-1][cc]:
                board[cr-1][cc] = board[cr][cc] + 1
                heappush(QUEUE, (cv+1, cr-1, cc))
        if cc-1 in range(C) and maps[cr][cc-1] != 0:
            if board[cr][cc] + 1 < board[cr][cc-1]:
                board[cr][cc-1] = board[cr][cc] + 1
                heappush(QUEUE, (cv+1, cr, cc-1))
        '''
    
    for line in board:
        print(line)
    
    answer = board[R-1][C-1]
    if answer == float('inf'):
        answer = -1
        
    return answer
