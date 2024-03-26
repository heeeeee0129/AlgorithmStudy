def solution(n, wires):
    def check(v):
        visited[v] = True
    
        for i in tree[v]:
            if not visited[i]:
                link[v] += check(i) + link[i]
        return 1

    answer = 100
    tree = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    link = [0] * (n+1)
    
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
        
    check(1)
    
    for i in link:
        answer = min(answer,abs(n-2*(i+1)))
    return answer
