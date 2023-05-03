# [3차] 2018 KAKAO BLIND RECRUITMENT


def solution(m, musicinfos):
    
    # 변수 생성
    answer = '(None)'
    musicLength = []
    musicName = []
    music = []
    tmplist = []
    flag = 0
    
    # 변수 값 지정
    for item in musicinfos:
        
        st, et, name, contents = item.split(',')
        sh, sm = map(int, st.split(':'))
        eh, em = map(int, et.split(':'))
        
        s = sh*60 + sm
        e = eh*60 + em
        
        musicLength.append(e-s)
        musicName.append(name)
        music.append('')
        
        while len(music[-1]) < musicLength[-1]:
            music[-1] += contents
            music[-1] = music[-1].replace('A#', 'a')
            music[-1] = music[-1].replace('C#', 'c')
            music[-1] = music[-1].replace('D#', 'd')
            music[-1] = music[-1].replace('F#', 'f')
            music[-1] = music[-1].replace('G#', 'g')
        music[-1] = music[-1][:musicLength[-1]]
    
    # '#' 처리
    m = m.replace('A#', 'a')
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    
    # m을 포함하는 음악 tmplist에 추가
    for i in range(len(music)):
        if m in music[i]:
            tmplist.append([musicName[i], musicLength[i]])
    
    # tmplist 중 제일 긴 음악 & 그 중 가장 앞에 있는 음악 answer에 대입
    for i in range(len(tmplist)):
        if tmplist[i][1] > flag:
            flag = tmplist[i][1]
            answer = tmplist[i][0]
    
    print(musicLength)
    print(music)
    print(tmplist)
    
    
    return answer
