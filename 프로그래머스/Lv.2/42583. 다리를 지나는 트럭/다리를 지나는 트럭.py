from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)
    time = 0
    current_weight = 0
    
    while truck_queue:
        time += 1
        current_weight -= bridge_queue.popleft()
        
        if current_weight+truck_queue[0] <= weight:
            current_weight += truck_queue[0]
            bridge_queue.append(truck_queue.popleft())
        else:
            bridge_queue.append(0)
    answer = time + bridge_length
    return answer