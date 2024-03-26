def solution(storey):
    answer = 0
    
    # 0층에 도달할 때까지 반복
    while storey > 0:
        n = storey % 10
        
        if n > 5:
            answer += 10 - n
            storey += 10 - n
        elif n == 5 and (storey//10)%10 >= 5:
            answer += 10 - n
            storey += 10 - n
        elif n > 0:
            answer += n
            storey -= n
            
        storey //= 10
    return answer
