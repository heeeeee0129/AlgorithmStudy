from collections import deque
def f(sr,sc,maps,visited):    
    row = [1,-1,0,0]
    col = [0,0,1,-1]  
    
    q = deque([(sr,sc)])
    visited[sr][sc] = 1
    days = int(maps[sr][sc])
    while q:
        m, n = q.popleft()
        
        for i in range(4):
            nr = m + row[i]
            nc = n + col[i]
            if 0<= nr < len(maps) and 0<= nc < len(maps[0]) and maps[nr][nc] != 'X' and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    days += int(maps[nr][nc])
                    q.append((nr,nc))
    return visited, days
    
def solution(maps):
    answer = []
    visited = [[0 for i in range(len(maps[0]))] for _ in range(len(maps))] # [[0]*len(maps[0])]*len(maps) 했더니 하나만 바꿔도 같이 바뀌는 문제 발생
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited, days = f(i,j,maps, visited)
                answer.append(days)
    if answer:
        answer.sort()   
    else:
        answer = [-1]
    return answer
