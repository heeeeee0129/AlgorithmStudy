import math
def solution(n):
    answer = ''
    # 3진법 쓰기
    while n > 0:
        n -= 1
        if n%3 == 0:
            answer = '1' + answer
        elif n%3 == 1:
            answer = '2' + answer
        elif n%3 == 2:
            answer = '4' + answer
        n = int(n/3) # n /= 3 했다가 잔뜩 실패났었음 ....
    return answer
