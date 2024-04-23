import heapq
import sys

def solution(N, road, K):
    answer = 0
    arr = [[] for _ in range(N+1)]
    for start, end, cost in road:
        arr[start].append([end, cost])
        arr[end].append([start, cost])
    queue = []
    dist = [sys.maxsize] * (N+1)
    heapq.heappush(queue, [0, 1]) # cost, node_number
    dist[1] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > dist[node]:
            continue
        for next_node, c in arr[node]:
            sum_cost = cost + c
            if sum_cost < dist[next_node]:
                dist[next_node] = sum_cost
                heapq.heappush(queue, [sum_cost, next_node])
    for d in dist:
        if d <= K:
            answer += 1
    
    return answer