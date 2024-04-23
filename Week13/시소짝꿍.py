from collections import Counter
def solution(weights):
    answer = 0
    freq = dict(Counter(weights))
    for i in freq:
        if freq[i] > 1:
            tmp = [i] * freq[i]
            answer += (freq[i]*(freq[i]-1)) //2
    li = [*freq]     
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] * 2 == li[j] or li[i] == li[j] * 2 or li[i] * 3 == li[j] * 2 or li[i] * 2 == li[j] * 3 or li[i] * 4 == li[j] * 3 or li[i] * 3 == li[j] * 4:
                answer += freq[li[i]]*freq[li[j]]
    
    return answer
