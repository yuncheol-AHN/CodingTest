# 세 수의 합을 구하는 과정

def solution(number):
    answer = 0
    
    student_length = len(number)
    
    
    for i in range(student_length - 2):
        for j in range(i + 1, student_length - 1):
            for k in range(j + 1, student_length):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer
