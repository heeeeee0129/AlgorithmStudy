from collections import deque
def solution(queue1, queue2):
    answer = 0
    sum1, sum2 = 0, 0
    origin = len(queue1)
    for i in queue1:
        sum1 += i
    for i in queue2:
        sum2 += i
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    count = 0
    while sum1 != sum2:
        if count > 2*origin+1: # 두 큐가 계속 스왑되는 경우가 불가능한 경우이며, 길이의 2배를 돌면 같아지기 직전까지 돌 수 있음 그래서 2*len +1 (사실 헷갈림 힝힝)
            answer = -1
            break
        if sum1 == 0 or sum2 == 0:
            answer = -1
            break
        # inter = abs((sum1 + sum2) / 2 - sum1)
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            answer += 1
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            answer += 1
            sum1 += tmp
            sum2 -= tmp
        count += 1
    return answer
