# 명예의 전당 List 생성
# 정확한 CASE 분류 -> 출연가수의 수가 k 이하일 때, k 이상일 때 -> 기존의 점수가 명예의 전당에 포함 될 때, 포함되지 않을 때

def solution(k, score):
    answer = []
    
    honor_list = []
    
    for item in score:
        if len(honor_list) == k:
            if honor_list[-1] > item:
                answer.append(honor_list[-1])
            else:
                honor_list.append(item)
                honor_list.sort(reverse=True)
                honor_list.pop()
                answer.append(honor_list[-1])
        else:
            honor_list.append(item)
            honor_list.sort(reverse=True)
            answer.append(honor_list[-1])
            
    return answer
