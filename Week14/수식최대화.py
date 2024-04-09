from itertools import permutations
from collections import deque
def calc(num1, ex, num2):
    if ex == '*':
        return num1 * num2
    elif ex == '+':
        return num1 + num2
    else:
        return num1 - num2

def solution(expression):
    answer = -1
    ops = []
    numbers = deque([])
    num = ''
    for c in expression:
        if c.isdigit():
            num += c
        else:
            numbers.append(int(num))
            num = ''
            numbers.append(c)
            ops.append(c)
    numbers.append(int(num))
    perms = permutations(set(ops))
    
    for p in perms:
        nums = deque(numbers.copy())
        for cur_op in p:
            stack = []
            while nums:
                cur = nums.popleft()
                if cur == cur_op:
                    res = calc(stack.pop(), cur, nums.popleft())
                    stack.append(res)
                else:
                    stack.append(cur)
            nums = deque(stack.copy())
            if len(nums) == 1:
                answer = max(answer, abs(nums.pop()))
                break
            
    return answer