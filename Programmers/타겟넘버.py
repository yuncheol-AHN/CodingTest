# from collections import deque
# deque 보다 스택이 더 빠름

def solution(numbers, target):
    
    answer = 0
    numbers_length = len(numbers)
    
    def dfs(idx, result):
        if idx == numbers_length:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result + numbers[idx])
            dfs(idx+1, result - numbers[idx])
    
    dfs(0, 0)
    
    return answer

'''
def solution(numbers, target):
    
    answer = 0
    length_numbers = len(numbers)
    
    def dfs(idx, value):
        idx += 1
        
        if idx < length_numbers:
            dfs(idx, value+numbers[idx])
            dfs(idx, value-numbers[idx])
        else:
            if target == value:
                nonlocal answer
                answer += 1
    
    dfs(0, numbers[0])
    dfs(0, -numbers[0])
    return answer
'''

