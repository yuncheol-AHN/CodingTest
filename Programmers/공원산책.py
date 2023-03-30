def solution(park, routes):
    answer = []
    position = [0, 0] # 1차원 배열
    table = park # 2차원 배열
    
    # table setting(S -> O), position initialize
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 'S':
                position = [i, j]
                table[i] = table[i].replace('S', 'O')
                break
    
    print(position)
    
    # routes cycle
    # 이동 가능 여부 판단 후 이동
    for item in routes:
        direction, distance = item.split()
        distance = int(distance)
        
        if direction == "E":
            print('E', distance, end=' ')
            
            if position[1] + distance < len(park[0]):
                flag = False
                
                for i in range(1, distance + 1):
                    if table[position[0]][position[1] + i] == 'X':
                        flag = True
                        break
                        
                if flag == False:
                    position[1] = position[1] + distance
                    
            print(position)
        elif direction == 'S':
            print('S', distance, end=' ')
            
            if position[0] + distance < len(park):
                flag = False
                
                for i in range(1, distance + 1):
                    if table[position[0] + i][position[1]] == 'X':
                        flag = True
                        break
                        
                if flag == False:
                    position[0] = position[0] + distance
                    
            print(position)
        elif direction == 'W':
            print('W', distance, end=' ')
            
            if position[1] - distance >= 0:
                flag = False
                
                for i in range(1, distance + 1):
                    if table[position[0]][position[1] - i] == 'X':
                        flag = True
                        break
                        
                if flag == False:
                    position[1] = position[1] - distance
                    
            print(position)
        elif direction == 'N':
            print('N', distance, end=' ')
            
            if position[0] - distance >= 0:
                flag = False
                
                for i in range(1, distance + 1):
                    if table[position[0] - i][position[1]] == 'X':
                        flag = True
                        break
                        
                if flag == False:
                    position[0] = position[0] - distance
                    
            print(position)
            
    answer = position
    return answer
