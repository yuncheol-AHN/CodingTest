
# 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    
    # 변수 생성
    answer = []
    pn = len(stages)
    percent = [(0, 0) for _ in range(N+1)]
    
    for i in range(N+1):
        
        son = 0
        mom = 0
        
        for stage in stages:
            if stage > i:
                mom += 1
            elif stage == i:
                mom += 1
                son += 1
        
        if mom != 0:
            percent[i] = (son / mom, i)
        else:
            percent[i] = (0, i)
    
    percent.pop(0)
    percent.sort(key = lambda x: (-x[0], x[1]))
    
    for i in percent:
        answer.append(i[1])
    
    print(percent)
    
    return answer
