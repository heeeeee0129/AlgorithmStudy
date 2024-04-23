def makeU(u):
    result = ''
    for c in u:
        if c == '(':
            result += ')'
        else:
            result += '('
    return result

def makeValid(w):
    count1 = 0
    count2 = 0
    for idx, c in enumerate(w):
        if c == '(':
            count1 += 1
        else:
            count2 += 1
        if count1 != 0 and count1 == count2:
            u = w[:idx+1]
            v = w[idx+1:]
            if isValid(u):
                return u + makeValid(v)
            else:
                return '(' + makeValid(v) + ')' + makeU(u[1:-1])
    return ''
    
def isValid(str):
    count = 0
    for c in str:
        if c == '(':
            count+=1
        else:
            count-=1
        if count < 0:
            return False
    if count == 0:
        return True
    return False


def solution(p):
    answer = makeValid(p)
    return answer

