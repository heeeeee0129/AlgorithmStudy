from collections import Counter
def solution(weights):
    answer = 0

    ops = [2/3, 3/4, 2/4]

    count = Counter(weights)
    for value in count.values():
        answer += value*(value-1) // 2

    weights = list(set(weights))

    for weight in weights:
        for op in ops:
            if weight*op in weights:
                answer += count[weight] * count[weight * op]

    return answer