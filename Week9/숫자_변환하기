# dfs는 11번 시간초과
def dfs(x, y, n, cur, num):
    if y == x:
        num.append(cur)
        return
    
    if y < x:
        return;
    
    if num != [] and cur >= min(num):
        return;
    
    if y % 2 == 0:
        recur(x, y//2, n, cur+1, num)
    if y % 3 == 0:
        recur(x, y//3, n, cur+1, num)
    
    recur(x, y-n, n, cur+1, num)

from collections import deque

def solution(x, y, n):
    num = [];
    
    queue = deque([(x,0)])
    visited = set()
    visited.add(x)
    
    while queue:
        current, depth = queue.popleft()

        if current == y:
            return depth
        
        if current * 3 not in visited and current * 3 <= y:
            queue.append((current * 3, depth + 1))
            visited.add(current * 3)
            
        if current * 2 not in visited and current * 2 <= y:
            queue.append((current * 2, depth + 1))
            visited.add(current * 2)


        if current + n <= y and current + n not in visited:
            queue.append((current + n, depth + 1))
            visited.add(current + n)
        
    
    return -1
