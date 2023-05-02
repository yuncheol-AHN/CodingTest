# 2018 KAKAO BLIND RECRUITMENT


def solution(n, t, m, timetable):
    
    # 변수 생성
    answer = ''
    timetable.sort()
    dict = {}
    lastElement = 0
    flag = False
    pushedTable = []
    
    # dictionary 생성
    for i in range(n):
        dict[540 + t*i] = m
        if i == n-1:
            lastElement = 540 + t*i
    
    # timetable : string -> int
    for i in range(len(timetable)):
        hour, minute = map(int, timetable[i].split(":"))
        timetable[i] = hour*60 + minute
    
    # timetable loop
    while timetable and dict[lastElement] != 0:
        
        # 탑승자가 마지막 시간보다 늦게 도착하면 반복문 탈출
        if timetable[0] > lastElement:
            break
        
        # 탑승할 수 있는 시간에 따라 탑승자 제거
        for key in dict:
            if key >= timetable[0] and dict[key] > 0:
                dict[key] -= 1
                pushedTable.append(timetable[0])
                timetable.pop(0)
                break
        
        
    # 조건에 따른 제일 늦은 시간
    if dict[lastElement] != 0:  # dictionary의 마지막 시간의 value가 0이 아닐 때 : 마지막 시간에 탑승 가능
        print(lastElement // 60, lastElement % 60)
        if (lastElement // 60) // 10 == 0:
            answer += "0" + str(lastElement // 60) + ":"
        else:
            answer += str(lastElement // 60) + ":"
        
        if (lastElement % 60) // 10 == 0:
            answer += "0" + str(lastElement % 60)
        else:
            answer += str(lastElement % 60)
    elif dict[lastElement] == 0: # dictionary의 마지막 시간의 value가 0 일 때, 마지막 인원 보다 1분 일찍 도착해야함
        tmp = pushedTable[-1] - 1
        if (tmp // 60) // 10 == 0:
            answer += "0" + str(tmp // 60) + ":"
        else:
            answer += str(tmp // 60) + ":"
            
        if (tmp % 60) // 10 == 0:
            answer += "0" + str(tmp % 60)
        else:
            answer += str(tmp % 60)
        
    return answer
