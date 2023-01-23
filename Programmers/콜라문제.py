def solution(a, b, n):
    answer = 0
    
    bottle_num = n
    
    while bottle_num >= a:
        answer += bottle_num // a * b
        bottle_num = bottle_num // a * b + bottle_num % a
    return answer
