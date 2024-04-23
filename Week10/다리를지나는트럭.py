from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    weights = deque(truck_weights)
    sum_weight = 0

    while weights or bridge: 
        answer+=1
        while bridge and bridge[0][0] == answer:
            out_truck = bridge.popleft()
            sum_weight-=out_truck[1]
        
        if weights:
            if sum_weight + weights[0] <= weight and len(bridge) < bridge_length:
                truck = weights.popleft()
                bridge.append(( bridge_length + answer, truck))
                sum_weight += truck
       
    return answer
