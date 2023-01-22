# 과일장수
# sort : reverse=True 사용가능
# slicing


def solution(k, m, score):
    answer = 0
    score_length = len(score)
    
    score.sort(reverse=True)
    
    for i in range(score_length // m):
        box = score[i*m:(i+1)*m]
        answer += min(box)*m 
    
    return answer
