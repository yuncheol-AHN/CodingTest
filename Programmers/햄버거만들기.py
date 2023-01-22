# 리스트에서 부분리스트 제거하기
# 시간복잡도 해결 : s = s[-4:] -> del s[-4:]

def solution(ingredient):
    answer = 0
    # 1 2 3 1
    s = []
    
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            # del s[-4:]
            for _ in range(4):
                s.pop()
        
    return answer
