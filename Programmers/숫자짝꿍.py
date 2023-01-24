# 숫자로 이루어진 문자열 -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]에 대입 : 시간복잡도 줄일 수 있다.
# set's interaction도 이용가능함.

def solution(X, Y):
    answer = ''
    
    X_list = [0 for _ in range(10)]
    Y_list = [0 for _ in range(10)]
    
    for i in X:
        X_list[int(i)] += 1
    
    for i in Y:
        Y_list[int(i)] += 1
    
    new_list = [0 for _ in range(10)]
    
    for i in range(10):
        new_list[i] = min(X_list[i], Y_list[i])
    
    for i in range(9, -1, -1):
        for _ in range(new_list[i]):
            answer += str(i)
            
    if len(answer) == 0:
        answer= "-1"
    
    if answer[0] == '0':
        while True:
            if '00' in answer:
                answer = answer.replace('00', '0')
            else:
                break
    
    return answer
