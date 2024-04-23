    for j in priority:
        while li:
            m = li.popleft()
            if m == j:
                q.append(str(eval(q.pop()+m+li.popleft())))
            else:
                q.append(m)
        li = deque(q)
    return int(li[-1])
def solution(expression):
    answer = 0
    start = 0
    li = []
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '*' or expression[i] == '+':
            li.append(expression[start:i])
            li.append(expression[i])
            start = i+1
    if start <= len(expression):
        li.append(expression[start:])
    poss = list(permutations(['*','-','+'],3))
    for i in poss:
        answer = max(abs(f(i,deque(li))), answer)
    return answer

