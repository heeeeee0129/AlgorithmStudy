import queue
def solution(order):
    # 보조 컨테이너 벨트는 stack(FILO), 컨테이너 벨트는 queue(FIFO)
    answer = 0
    assist = []
    main = queue.Queue()
    idx = 0
    for i in range(len(order)):
        main.put(i+1) # 메인 컨테이너 벨트에 택배상자 넣기
        
    while idx < len(order):
        if main.qsize() == 0 and assist and assist[-1] != order[idx]:
            break # 더이상 진행할 수 없는 경우 종료 
        if assist and assist[-1] == order[idx]: # 보조 컨테이너벨트에 있는 경우
            answer += 1
            idx += 1
            assist.pop()
        else:
            item = main.get()
            if item == order[idx]: # 컨테이너 벨트에 있는 경우
                answer += 1
                idx += 1
            else: # 없을 경우 해당 아이템 보조 컨테이너벨트에 저장
                assist.append(item)
    return answer
