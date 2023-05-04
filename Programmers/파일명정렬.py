# [3차] 2018 KAKAO BLIND RECRUITMENT

def solution(files):
    
    # HEAD : 정렬 / 대소문자 구분X
    # NUMBER : 정렬
    # HEAD, NUMBER 우선순위 일치 -> 들어온 순서로 출력
    
    # 변수 설정
    answer = []
    orderedFiles = [] # (HEAD, NUMBER, TAIL)로 이루어진 튜플 배열
    order = []        # 파일의 순서를 담은 배열
    n = 0             # 우선순위가 같을 경우, 먼저 들어온 값에 높은 우선순위를 주기위한 변수
    
    # Loop -> orderedFiles 생성
    for file in files:
        
        idxNumber = 0   # NUMBER 시작 위치
        numberSize = 0  # NUMBER의 크기 : 1 - 5
        
        # file 분석
        for i in range(len(file)):
            
            # file에서 숫자를 처음 만날 때, i에서
            if file[i].isdigit():
                idxNumber = i
                
                # i부터 file의 끝까지 확인하며 number size 구하기
                for j in range(i, len(file)):
                    # size > 5 or 숫자가 아닐 때, 탈출
                    if numberSize > 5:
                        break
                    if file[j].isdigit():
                        numberSize += 1
                    else:
                        break
                        
                break
                
        # idxTail, ordered files
        idxTail = idxNumber + numberSize
        orderedFiles.append((file[:idxNumber].upper(), int(file[idxNumber:idxTail]), n, file[idxTail:]))
        n += 1
    
    orderedFiles.sort()
    # print(orderedFiles)
    
    for i in orderedFiles:
        order.append(i[2])
    # print(order)
    
    # order(순서)에 따라 answer 배열에 file 추가
    for i in order:
        answer.append(files[i])
    
    return answer
