# 거꾸로
# range(9, -1, -1) : 9 8 7 ... 0
# range(10, 0, -1) : 10 9 8 ... 1

def solution(s):
    answer = []
    
    arr = []
    s_length = len(s)
    
    for idx in range(s_length):
        if s[idx] in arr:
            for i in range(idx - 1, -1, -1):
                if s[i] == s[idx]:
                    answer.append(idx - i)
                    break
        else:
            arr.append(s[idx])
            answer.append(-1)
             
    return answer
