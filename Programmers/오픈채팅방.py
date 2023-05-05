# 2019 KAKAO BLIND RECRUITMENT

def solution(record):
    answer = []
    tmp = []
    dict = {}
    
    for r in record:
        l = r.split(' ')
        
        if l[0] == 'Enter':
            tmp.append(l[1] + " 님이 들어왔습니다.")
            dict[l[1]] = l[2]
        elif l[0] == 'Leave':
            tmp.append(l[1] + " 님이 나갔습니다.")
        elif l[0] == 'Change':
            dict[l[1]] = l[2]
    
    for i in range(len(tmp)):
        l = tmp[i].split()
        answer.append(dict[l[0]] + l[1] + ' ' + l[2])
    
    return answer
