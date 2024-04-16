def solution(queue1, queue2):
    answer = 0
    
    q = queue1 + queue2
    middle = sum(q)//2
    
    # 값 하나가 중앙값보다 큰 경우 목표 달성 불가
    if max(queue1) > middle or max(queue2) > middle:
        return -1
    
    start, end = 0, len(queue1)
    s = sum(q[start:end])
    
    # queue1과 queue2를 붙인 후 middle과 값이 다른 경우 한 칸 추가하거나 삭제하여 Middle과 동일하게 맞추기
    # 칸이 변경될 때는 무조건 answer+1
    while start < len(q):
        if s == middle:
            break
        if s < middle and end < len(q):
            s += q[end]
            end += 1
            answer += 1
        else :
            s -= q[start]
            start += 1
            answer += 1
    
    if start >= len(q):
        return -1
            
    return answer
