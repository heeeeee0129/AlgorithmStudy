def solution(x, y, n):
    answer = 0
    list = set()
    list.add(x)
    while True:
        tmp = set()
        if y in list:
            return answer
        for i in list:
            if i+n == y or 2*i == y or 3*i == y:
                answer +=1
                return answer
            if i+n < y:
                tmp.add(i+n)
            if 2*i < y:
                tmp.add(2*i)
            if 3*i < y:
                tmp.add(3*i)
        if all(j>y for j in tmp):
            return -1
        answer += 1
        list = tmp
    return answer
