# 문자열 나누기
# 비교를 위한 변수 left, right 설정
# 비교를 위한 idx 정확히 계산

def solution(s):
    answer = 0
    
    s_length = len(s)
    x = s[0]
    left = 0
    right = 0
    
    for idx in range(s_length):
        if s[idx] == x:
            left += 1
        else:
            right += 1
        
        if idx+1 == s_length:
            answer += 1
            break
        elif left == right and left != 0:
            answer += 1
            left = 0
            right = 0
            x = s[idx+1]
        
    
    return answer
