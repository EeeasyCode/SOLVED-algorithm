from collections import deque

def solution(priorities, location):
    answer = 0
    pq = deque(priorities)    
    
    while pq:
        m = max(pq)
        pop = pq.popleft()
        location -= 1
        
        if m != pop:
            pq.append(pop)
            if location < 0:
                location = len(pq) - 1
        else:
            answer += 1
            if location < 0:
                break
    return answer