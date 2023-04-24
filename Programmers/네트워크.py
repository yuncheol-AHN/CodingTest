# 네트워크, BFS

def solution(n, computers):
    count = 0
    queue = []
    
    # net seems like maps
    net = [1 for _ in range(n)]
    graph = [[] for _ in range(n)]
    
    # modify computers[i][i]
    for i in range(n):
        computers[i][i] = 0
    
    # graph
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    # BFS
    for i in range(n):
        if net[i] == 1:
            net[i] = 0
            queue.append(i)
            
            while queue:
                start = queue.pop(0)
                for e in graph[start]:
                    if net[e] == 1:
                        net[e] = 0
                        queue.append(e)
            count += 1
                
    return count
