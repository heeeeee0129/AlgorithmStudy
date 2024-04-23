def f(visited,li,start):
    q = [start]
    while q:
        st = q.pop(0)
        tmp = sorted(li[st],key=lambda x:x[1])
        for m,n in tmp:
            if visited[m] == -1 or visited[m] > visited[st] + n:
                visited[m] = visited[st] + n
                q.append(m)
    return visited
def solution(N, road, K):
    answer = 0
    
    li = [[] for _ in range(N+1)]
    for i, j, k in road:
        li[i].append((j,k))
        li[j].append((i,k))
    visited = [-1 for _ in range(N+1)]
    visited[1] = 0
    visited = f(visited,li,1)  
    for i in range(1,len(visited)):
        if visited[i] <= K:
            answer += 1
    return answer
