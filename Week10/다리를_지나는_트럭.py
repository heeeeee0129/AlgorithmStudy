def solution(bridge_length, weight, truck_weights):
    answer = 0
    # hash를 이용해서 다리를 건너는데 얼마나 걸리는지 확인? -> 같은 값이 존재해서 key로 구분 불가
    moving_truck = []
    # 모두 다리를 지난 경우에 나온다
    while truck_weights or moving_truck:
        answer += 1
        s = [truck[0] for truck in moving_truck] if moving_truck else []
        s = sum(s)
        
        # 트럭이 더 다리를 건널 수 있는 경우 트럭 추가
        if len(moving_truck) < bridge_length and truck_weights and s + truck_weights[0] <= weight:
            moving_truck.append([truck_weights[0], 0])
            truck_weights.pop(0)
            
        delMove = -1
        # 모든 트럭에 다리를 건너는 시간을 더한 후 다리를 지났다면 다리를 건너는 트럭에서 삭제
        for idx in range(len(moving_truck)):
            moving_truck[idx][1] += 1
            if moving_truck[idx][1] >= bridge_length:
                delMove = idx
                
        if delMove >= 0:
            moving_truck.pop(delMove)
        
    # 마지막 트럭이 다리를 나오는 도중 while이 끝나므로 시간 +1 
    return answer+1
