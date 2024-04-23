from itertools import permutations 

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers)+1):
        nums+=list(int(''.join(i)) for i in permutations(numbers,i))
    nums = set(nums)
    print(nums)
    
    for num in nums:
        if is_prime_number(num):
            print(num)
            answer += 1
            
    return answer