from itertools import combinations

def solution(orders, course):
    answer = []
    
    # 코스에 넣을 음식 별로 추가
    for num in course:
        l = []
        c = dict()
        
        # 모든 주문 조합을 l에 저장
        for order in orders:
            order = sorted(order)
            combs = list(combinations(order, num));
            for comb in combs:
                l.append(''.join(comb))
        
        # l에 저장된 주문들로 겹치는 주문 수 체크
        for order in l:
            if order in c:
                c[order] += 1
            else:
                c[order] = 1
        
        # 2번 이상 주문되고 제일 많이 주문된 음식 저장
        m = max(c.values()) if c else 0
        if m >=2:
            for cou in c:
                if c[cou] == m:
                    answer.append(cou)
    
    return sorted(answer)
