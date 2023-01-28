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
