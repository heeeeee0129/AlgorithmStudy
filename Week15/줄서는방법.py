
import math

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    
    while arr:
        f = math.factorial(len(arr)-1)
        
        if k % f == 0:
            index = k//f-1
        else:
            index = k//f
        answer.append(arr.pop(index))
        k = k % f

    return answer