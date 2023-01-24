# 문자열 대체 후 진위 체크를 어떻게 할 것인가 !!!
# replace method -> 리스트에서 사용 불가. 문자열에서 선택된 모든 문자를 대체문자로 바꾼다.

def solution(babbling):
    answer = 0
    
    words = ['aya', 'ye', 'woo', 'ma']
    repeats = ['ayaaya', 'yeye', 'woowoo', 'mama']
    
    for item in babbling:
        for repeat in repeats:
            item = item.replace(repeat, 'X')
        for word in words:
            item = item.replace(word, 'O')
        
        isValue = True
        for char in item:
            if char != 'O':
                isValue = False
        
        if isValue == True:
            answer += 1
    
    return answer
