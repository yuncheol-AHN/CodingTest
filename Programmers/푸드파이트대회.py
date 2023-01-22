# 문자열 뒤집기 [::-1]
# 집중해서 정확한 실행의 흐름을 파악해야함. 중간에 빼먹는 것들이 많음...


def solution(food):
    answer = ''
    
    food_length = len(food)
    food_couple = []
    for idx in range(food_length):
        if idx == 0:
            if food[idx] % 2 == 0:
                food_couple[idx] = food[idx] - 1
        else:
            if food[idx] % 2 != 0:
                food_couple[idx] = food[idx] - 1
    
    left_string = ""
    right_string = ""
    
    for idx in range(1, food_length):
        for _ in range(food_couple[idx]//2):
            left_string += str(idx)
    
    right_string = left_string
    
    for _ in range(food_couple[0]):
        left_string += "0"
    
    answer = left_string + right_string[::-1]
    
    
    return answer
