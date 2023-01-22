# 기사단원의 무기
# 약수를 구하는 함수 -> 시간복잡도, 일반적으로 O(N), O(N**(1/2))
# x**y = x의 y승
# 필요로하는 범위 정확히 체크, 0 ... n-1 인지 1 ... n 인지

def devisior(number):
    if number == 1:
        return 1
    
    result = 1
    for i in range(1, number):
        if number % i == 0:
            result += 1
    
    return result

def solution(number, limit, power):
    answer = 0
    
    for item in range(1, number + 1):
        devisior_number = devisior(item)
        if devisior_number > limit:
            answer += power
        else:
            answer += devisior_number
    
    return answer
