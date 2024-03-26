from itertools import combinations
def solution(orders, course):
    answer = []
    combi = {}
    # 모든 orders에서 가장 많이 나온 거 찾기(여러 개일 수 있음->예시 3번), 그리고 해당 조합이 2번 이상 나와야함
    # 모든 조합을 combinations를 이용해서 하나씩 반복문을 돌면서 있으면 dict의 값을 1 증가하고, 없으면 dict에 추가하기
    for i in orders:
        for j in course:
            tmp = combinations(i,j)
            for k in tmp:
                word = ''.join(sorted(''.join(k)))
                if word in combi:
                    combi[word] += 1
                else:
                    combi[word] = 1
    sorted_combi = sorted(combi.items(), key=lambda x: -x[1])
    many = {len(sorted_combi[0][0]):sorted_combi[0][1]}
    for key, val in sorted_combi:
        if len(key) in many and many[len(key)] == val and val > 1:
            answer.append(key)
        elif len(key) not in many and val > 1:
            many[len(key)] = val
            answer.append(key)
            
    # 결과는 오름차순으로 정렬해서 반환하기
    answer.sort()
    return answer
