from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        row = list(maps[i])
        maps[i] = row

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                sum_day = int(maps[i][j])
                q = deque()
                q.append([i, j])
                while q:
                    curx, cury = q.popleft()
                    maps[curx][cury] = 'X';
                    for d in range(4):
                        next_x, next_y = curx+dx[d], cury+dy[d]
                        if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] != 'X':
                            sum_day += int(maps[next_x][next_y])
                            maps[next_x][next_y] = 'X'
                            q.append([next_x, next_y])
                answer.append(sum_day)

    return sorted(answer) if answer else [-1]