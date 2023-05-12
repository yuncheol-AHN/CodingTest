# 2020 카카오

def solution(s):
    
    # 변수 설정
    answer = 1001
    half_length_s = len(s) // 2
    
    # 압축 단위에 따른 반복문
    for n in range(1, half_length_s + 1):
        re = [s[i:i+n] for i in range(0, len(s), n)]
        
        # 압축 단위 + 횟수를 담은 배열
        arrays = [('', 0)]
        for item in re:
            
            if arrays[-1][0] == item:
                arrays[-1][1] += 1
            else:
                arrays.append([item, 1])
        
        # 길이 구하기
        tmp = 0
        for k, v in arrays:
            tmp += len(k)
            if v > 1:
                tmp += len(str(v))
        
        # 최소값 구하기
        answer = min(tmp, answer)
        
    return answer
