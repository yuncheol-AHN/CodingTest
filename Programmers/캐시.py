# 2018 KAKAO BLIND RECRUITMENT
# 예외 처리 ... 어렵다 ...

def solution(cacheSize, cities):
    
    # 변수
    answer = 0
    stk = []
    
    # Loop
    for item in cities:
        
        # 대문자로 통일
        item = item.upper()
        
        # 캐시에 존재하면 +1, 그렇지 않으면 +5
        if item in stk:
            answer += 1
        else:
            answer += 5
                
        # 스택에 존재하지 않으면 스택에 도시 추가 / 스택에 존재하면 제거 후 추가
        if item not in stk:
            stk.append(item)
        else:
            stk.remove(item)
            stk.append(item)
        
        # 스택 사이즈가 캐시 사이즈 보다 크면 pop(0)
        if len(stk) > cacheSize:
            stk.pop(0)
            
    return answer
