# [3차] 2018 KAKAO BLIND RECRUITMENT

def solution(msg):
    
    # 변수 생성
    answer = []
    dict = {}
    idx = 0
    l = 0
    
    # 사전 생성
    for n in range(1, 27):
        dict[chr(n + 64)] = n   # ASCII : 65 -
    
    # 반복문
    while True:
        
        l += 1
        
        if msg[idx: idx+l] not in dict:
            answer.append(dict[msg[idx: idx + l - 1]])
            dict[msg[idx: idx + l]] = len(dict) + 1
            idx += l - 1
            l = 0
            
        else:
            if idx + l - 1 == len(msg):
                answer.append(dict[msg[idx: idx + l - 1]])
                break
                
    return answer
