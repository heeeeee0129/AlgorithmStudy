def gcd(a,b): # 유클리드 호제법 이용 
        # "2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때, a와 b의 최대공약수는 b와 r의 최대공약수와 같다."
    while b:
        a, b = b, a % b
        yield a
def solution(arrayA, arrayB):
    answer = 0
    isDivA, isDivB = False, False
    tmpA, tmpB = -1, -1            
    divA = arrayA[0]
    for i in range(1,len(arrayA)):
        divA = list(gcd(divA,arrayA[i]))[-1]
    divB = arrayB[0]
    for i in range(1, len(arrayB)):
        divB = list(gcd(divB, arrayB[i]))[-1]
    if divA != 1: # arrayA에서 모든 숫자를 나눌 수 있는 숫자가 있음
        for i in arrayB:
            if i % divA == 0:
                isDivA = True
    if divB != 1: # arrayB에서 모든 숫자를 나눌 수 있는 숫자가 있음
        for i in arrayA:
            if i % divB == 0:
                isDivB = True
    if not isDivA and divA != 1:
        tmpA = divA
    if not isDivB and divB != 1:
        tmpB = divB
    if tmpA == -1 and tmpB == -1: # divA와 divB가 모두 -1이라는 의미로 가능한 숫자가 없음
        answer = 0
    else:
        if tmpA >= tmpB: 
            answer = tmpA
        else:
            answer = tmpB
    return answer
