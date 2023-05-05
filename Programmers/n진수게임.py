
# [3차] 2018 KAKAO BLIND RECRUITMENT

def solution(n, t, m, p):
    
    # 변수 생성
    answer = ''
    nString = ''
    
    # N진수 구하는 함수
    def nJinsu(num, n):
        
        if num == 0:
            return '0'
        
        s = ''
        
        while num > 0:
            
            # 11진수 이상에서의 예외 처리
            if num%n >= 10:
                s += chr(55 + num%n)
            else:
                s += str(num%n)
                
            num = num // n
        
        return s[::-1]
    
    # 튜브가 말해야하는 값까지의 문자열 구성
    i = 0
    while len(nString) < m*(t+1):
        nString += nJinsu(i, n)
        i += 1
    
    # 튜브가 말해야하는 값 answer에 추가
    for i in range(t):
        answer += nString[i*m + (p-1)]
    
    return answer
