
def solution(order):
    answer = 0
    stack = [0]*len(order)
    for idx, value in enumerate(order):
        stack[len(order)-value] = idx+1
    sub = []
    index = 1
    while stack:
        while sub and sub[-1] == index:
            sub.pop()
            index+=1
        if stack[-1] == index:
            stack.pop()
            index += 1
        else:
            sub.append(stack.pop())
    while sub and sub[-1] == index:
        sub.pop()
        index+=1  
    
    return index-1