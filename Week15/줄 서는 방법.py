def solution(n, k):
    answer = []
    k -= 1
    l = [i for i in range(1, n+1)]
    d = 1
    
    for i in range(2, n):
        d *= i
        
    while n > 1:
        answer.append(l[int(k//d)])
        del l[int(k//d)]
        n -= 1
        k %= d
        d = int(d//n)
    
    answer.append(l[0])
        
    return answer
