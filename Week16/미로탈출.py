from collections import deque 
def f(maps,sr,sc,er,ec):
    
    q = deque([(sr,sc)])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    row = [0,0,1,-1]
    col = [1,-1,0,0]
    
    while q:
        m, n = q.popleft()
        for i in range(4):
            r = m + row[i]
            c = n + col[i]
            if -1<r<len(maps) and -1<c<len(maps[0]) and visited[r][c] == 0 and maps[r][c] != 'X':
                q.append((r,c))
                visited[r][c] = visited[m][n]+1
                if r == er and c == ec:
                    return visited[r][c]
    return -1

def solution(maps):
    answer = 0

    sr, sc = 0, 0
    lr, lc = 0, 0
    er, ec = 0, 0
    time1, time2 = 0, 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sr = i
                sc = j
            elif maps[i][j] == 'L':
                lr = i
                lc = j
            elif maps[i][j] == 'E':
                er = i
                ec = j
    time1 = f(maps, sr, sc, lr, lc)
    time2 = f(maps, lr, lc, er, ec)
    if time1 == -1 or time2 == -1:
        return -1
    return time1+time2
