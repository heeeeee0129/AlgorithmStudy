def solution(number, k):
    answer = ''
    kList = [i for i in range(k)]
    number = list(number)
    stack = []
    
    for idx, num in enumerate(number):
        if stack == []:
            stack.append(num)
        elif len(stack) == idx - k:
            stack.append(num)
            
        elif stack[-1] < num:
            while stack != [] and len(stack) != idx-k and stack[-1] < num:
                stack.pop(-1)
            stack.append(num)
        elif len(stack) < len(number)-k:
            stack.append(num)
            
            
    return ''.join(stack)
