def solution(sequence, k):
    sum = 0
    right = 0
    possList = []
    for idx, val in enumerate(sequence):
        if val == k:
            possList.append((idx,idx,0))
            return [idx,idx]
        while sum < k and right < len(sequence):
            sum += sequence[right]
            right += 1
        if sum == k:
            possList.append((idx,right-1,right-idx))
        sum -= val
    possList.sort(key = lambda x:x[2])
    answer = [possList[0][0],possList[0][1]]
    return answer
