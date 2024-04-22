from collections import deque

def solution(places):
    answer = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                # 탐색 시작
                    visited = [[False]*5 for _ in range(5)]
                    q = deque()
                    q.append([i, j, 0])
                    
                    while q and not flag:
                        x, y, count = q.popleft()
                        if count == 2:
                            continue
                        visited[x][y] = True
                        for d in range(4):
                            curx = x + dx[d]
                            cury = y + dy[d]
                            if 0 <= curx < 5 and 0 <= cury < 5 and not visited[curx][cury]:
                                if place[curx][cury] == 'O':
                                    q.append([curx, cury, count+1])
                                elif place[curx][cury] == 'P':
                                    flag = True
                                    break
        answer.append(1) if not flag else answer.append(0)
                        
    return answer