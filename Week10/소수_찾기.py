import itertools
import math

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    l = []
    for length in range(1, len(numbers)+1):
        pers = list(itertools.permutations(numbers, length))
        for item in pers:
            num = int(''.join(item))
            if num not in l and num > 1:
                l.append(num)
                
    for num in l:
        dnum = 2
        while dnum <= math.sqrt(num):
            if num % dnum == 0:
                break;
            dnum += 1
                
        if dnum > math.sqrt(num):
            answer += 1
    
    return answer
