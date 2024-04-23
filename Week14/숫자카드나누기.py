from collections import deque

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a*b)//math.gcd(a, b)

def solution(arrayA, arrayB):
    a = deque(arrayA)
    b = deque(arrayB)
    while len(a) > 1:
        res = gcd(a.popleft(), a.popleft())
        a.append(res)
    while len(b) > 1:
        res = gcd(b.popleft(), b.popleft())
        b.append(res)
    
    gcdA = a[0]
    gcdB = b[0]
    
    if gcdA == 1 and gcdB == 1:
        return 0
    
    flag1 = True
    for num in arrayA:
        if num % gcdB == 0:
            flag1 = False
            break
    flag2 = True
    for num in arrayB:
        if num % gcdA == 0:
            flag2 = False
            break
    if flag1:
        if flag2:
            return max(gcdA, gcdB)
        else:
            return gcdB
    elif flag2:
        return gcdA
    return 0
    

