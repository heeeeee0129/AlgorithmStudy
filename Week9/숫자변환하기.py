from collections import deque

def solution(x, y, n):
    
    q = deque()
    q.append((y, 0))
    while q:
        num, count = q.popleft()
        if num == x:
            return count
        if num < x:
            continue
        if num % 3 == 0:
            q.append((num//3, count+1 ))
        if num % 2 == 0:
            q.append((num//2, count+1))
        q.append((num-n, count+1))
        
    
    return -1