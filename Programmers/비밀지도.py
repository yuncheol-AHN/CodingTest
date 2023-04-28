
# 2018 KAKAO BLIND RECRUITMENT
# 문자열, 리스트 다루기

def solution(n, arr1, arr2):
    
    # 변수 생성
    answer = []
    maps = [[0 for _ in range(n)] for _ in range(n)]
    map1, map2 = [], []
    
    # arr1 -> map1
    for i in arr1:
        l = ''
        while i > 0:
            l = str(i%2) + l
            i = i // 2
        
        while len(l) < n:
            l = '0' + l
        
        map1.append(list(l))
    
    # arr2 -> map2
    for i in arr2:
        l = ''
        while i > 0:
            l = str(i%2) + l
            i = i // 2
        
        while len(l) < n:
            l = '0' + l
        
        map2.append(list(l))
    
    # map1 & map2 -> maps
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '0' and map2[i][j] == '0':
                maps[i][j] = ' '
            else:
                maps[i][j] = '#'
    
    # maps(list) -> answer(string)
    for item in maps:
        answer.append(''.join(item))
        
    return answer
