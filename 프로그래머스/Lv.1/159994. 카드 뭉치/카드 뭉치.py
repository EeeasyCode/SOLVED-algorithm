from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    c1_queue = deque(cards1)
    c2_queue = deque(cards2)
    cnt = 0
    
    for g in goal:
        if c1_queue and g == c1_queue[0]:
            cnt += 1
            c1_queue.popleft()
        elif c2_queue and g == c2_queue[0]:
            cnt += 1
            c2_queue.popleft()
    
    if cnt == len(goal):
        return "Yes"
    else:
        return "No"
    return answer