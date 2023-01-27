# 소수개수 구하기
# N진법

import math

def solution(n, k):
    answer = 0
    
    number = ''
    
    while n > 0:
        number += str(n%k)
        n = n//k
    
    number = number[::-1]
    
    number_list = number.split('0')
    
    while True:
        if '' in number_list:
            number_list.remove('')
        else:
            break
    
    for x in number_list:
        num = int(x)
        check = 0
        
        if num < 2:
            continue
        elif num == 2:
            answer += 1
            continue
            
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                check += 1
        
        if check > 0:
            continue
        elif check == 0:
            answer += 1
    
    
    return answer
