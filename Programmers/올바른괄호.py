# stack, queue : append, pop
# CASE 분류

def solution(s):
    answer = True
    
    list = []
    for i in s:
        if i == '(':
            list.append('(')
        elif i == ')':
            if len(list) == 0:
                return False
            else:
                list.pop()
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if len(list) > 0:
        return False
    else:
        return True
