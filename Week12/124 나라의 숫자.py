def solution(n):
    answer = ''
    number = ["4", "1", "2"]
    
    while (n >= 3):
        answer = number[n%3] + answer
        if n%3 == 0:
            n -= 1
        n =int(n/3)
        
    if n>0:
        answer = number[n] + answer
    return answer
