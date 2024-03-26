def solution(n):
    
    l = [0]*(n+1)
    l[1] = 1
    l[2] = 1
    for i in range(3, n+1):
        l[i] = (l[i-1]+l[i-2])%1000000007
            
    
    return (l[n]+l[n-1])%1000000007
