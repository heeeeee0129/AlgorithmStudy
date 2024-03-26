def solution(order):
    answer = 0
    want = 0
    bozo = []
    for idx in range(1, len(order)+1):
        # 트럭에 넣을 수 없으면 보조 컨테이너에 넣고 다음으로
        if idx != order[want]:
            bozo.append(idx)
            continue;
            
        # 바로 트럭에 넣을 수 있으면 택배기사한테 주기
        if idx == order[want]:
            answer += 1
            want += 1
        
        # 보조에서 꺼낼 수 있는 게 있는지 확인
        while bozo and order[want] == bozo[-1]:
            
            answer += 1
            want += 1
            bozo.pop()
            continue;
            
        
    return answer
