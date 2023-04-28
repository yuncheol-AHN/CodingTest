# 2018 KAKAO BLIND RECRUITMENT
# 구현 ?

def solution(m, n, board):
    
    # 변수 생성
    answer = 0
    stk = []
    flag = True
    
    # 문자열 리스트 -> 2차원 리스트
    for i in range(m):
        board[i] = list(board[i])
    
    # Loop
    while flag:
        flag = False
        
        # 제거해야하는 블록(2X2)의 좌상단 값을 스택에 저장
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != ' ' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    stk.append([i, j])
                    flag = True

        # print(stk)
        
        # 스택을 돌며, 제거해야할 블록을 공백(' ') 처리
        while stk:
            i, j = stk.pop()
            for x, y in ((i, j), (i+1, j), (i, j+1), (i+1, j+1)):
                board[x][y] = ' '

        #for e in board:
        #    print(e)
        #print()

        # 빈 블록을 위로, 그렇지 않은 블록을 아래로
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if board[i][j] == ' ':
                    for up in range(i-1, -1, -1):
                        if board[up][j] != ' ':
                            board[i][j] = board[up][j]
                            board[up][j] = ' '
                            break

        #for e in board:
        #    print(e)
    
    # 빈 블록 개수 만큼 answer += 1
    for i in range(m):
        for j in range(n):
            if board[i][j] == ' ':
                answer += 1
    
    return answer
