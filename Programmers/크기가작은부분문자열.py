
# 문자열 슬라이싱

def solution(t, p):
    answer = 0
    
    t_length = len(t)
    p_length = len(p)
    
    for i in range(t_length - p_length + 1):
        if int(t[i:i+p_length]) <= int(p):
            answer += 1
        
    
    return answer
