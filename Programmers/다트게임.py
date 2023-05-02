# 2018 KAKAO BLIND RECRUITMENT
# 예외 처리

def solution(dartResult):
    
    # 변수 생성
    answer = 0
    stkDigit = []
    stkBonus = []
    stkSum = []
    
    # dartResult -> stkDigit, stkBonus
    for e in dartResult:
        
        if e.isdigit() == True: # dartResult -> stkDigit
            stkDigit.append(e)
        else:   # dartResult -> stkBonus
            stkBonus.append(e)
        
        # 숫자 10 처리하는 조건문
        if len(stkDigit) >= 2:
            if stkDigit[-2] == '1' and stkDigit[-1] == '0':
                stkDigit.pop()
                stkDigit[-1] = '10'
    
    # stkDigit, stkBonus에서 빼낸 값을 계산해 stkSum에 저장
    while stkDigit and stkBonus:
        
        # digit, bonus, option 추출
        digit = int(stkDigit.pop(0))
        bonus = stkBonus.pop(0)
        option = ''
        
        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        elif bonus == 'T':
            bonus = 3
        
        if stkBonus:
            if stkBonus[0] == '*' or stkBonus[0] == '#':
                option = stkBonus.pop(0)
        
        # digit, bonus, option를 통해 계산
        if digit == 0:
            tmp = 0
        else:
            tmp = pow(digit, bonus)
            
        if option == '*':
            tmp *= 2
            if stkSum:
                stkSum[-1] *= 2
        elif option == '#':
            tmp *= -1
        
        # 계산한 값(tmp)를 stkSum에 저장
        stkSum.append(tmp)
    
    answer = sum(stkSum)
    
    return answer
