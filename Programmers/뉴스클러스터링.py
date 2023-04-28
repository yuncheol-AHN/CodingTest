# 2018 KAKAO BLIND RECRUITMENT
# dictionary

def solution(str1, str2):
    
    # 변수 생성
    answer = 0
    keyNumber = 65536
    
    # dictionary1, dictionary2
    dict1 = {}
    dict2 = {}
    
    # str1 -> dictionary1
    for i in range(0, len(str1)-1):
        item = str1[i:i+2].upper()
        if item.isalpha():
            if item not in dict1:
                dict1[item] = 1
            else:
                dict1[item] += 1
    
    # str2 -> dictionary2
    for i in range(0, len(str2)-1):
        item = str2[i:i+2].upper()
        if item.isalpha():
            if item not in dict2:
                dict2[item] = 1
            else:
                dict2[item] += 1
    
    # intersection length, union length
    intersectionLength = 0
    unionLength = 0
    
    for i in dict1:
        if i in dict2:
            intersectionLength += min(dict1[i], dict2[i])
            unionLength += max(dict1[i], dict2[i])
        else:
            unionLength += dict1[i]
            
    for i in dict2:
        if i not in dict1:
            unionLength += dict2[i]
    
    # exception handling
    if unionLength == 0:
        answer = keyNumber
    else:
        answer = keyNumber * (intersectionLength / unionLength)
    
    return int(answer)
