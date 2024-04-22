from collections import deque

def solution(maps):
    toStart = -1
    toEnd = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    
    lever = []
    for i in range(n):
        maps[i] = list(maps[i])
        print(maps[i])
        for j in range(m):
            if maps[i][j] == 'L':
                lever = [i,j]
                break
    
    queue = deque([])
    visited = [[False]*m for _ in range(n)]
    queue.append([0, lever[0], lever[1]])
    visited[lever[0]][lever[1]] = True
    while queue:
        cost, x, y = queue.popleft()
        
        for d in range(4):
            curx = x + dx[d]
            cury = y + dy[d]
            if 0 <= curx < n and 0 <= cury < m and not visited[curx][cury] and maps[curx][cury] != 'X':
                if maps[curx][cury] == 'S':
                    toStart = cost+1
                    break
                queue.append([cost+1, curx, cury])
                visited[curx][cury] = True
        if toStart != -1:
            break
                
    queue = deque([])
    visited = [[False]*m for _ in range(n)]
    queue.append([0, lever[0], lever[1]])
    visited[lever[0]][lever[1]] = True
    while queue:
        cost, x, y = queue.popleft()
        
        for d in range(4):
            curx = x + dx[d]
            cury = y + dy[d]
            
            if 0 <= curx < n and 0 <= cury < m and not visited[curx][cury] and maps[curx][cury] != 'X':
                if maps[curx][cury] == 'E':
                    toEnd = cost+1
                    break
                queue.append([cost+1, curx, cury])
                visited[curx][cury] = True
        if toEnd != -1:
            break
    if toStart < 0 or toEnd < 0 :
        return -1
    print(toStart, toEnd)
    return toStart+toEnd