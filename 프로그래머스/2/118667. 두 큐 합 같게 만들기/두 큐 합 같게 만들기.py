from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    
    if sum(queue1+queue2)%2!=0:
        return -1
    sum1, sum2 = sum(queue1), sum(queue2)
    cnt=0
    for _ in range(len(queue1)*3):
        if sum1 > sum2:
            cnt+=1
            val = queue1.popleft()
            sum1 -= val
            sum2 += val
            queue2.append(val)
        elif sum1 < sum2:
            cnt+=1
            val = queue2.popleft()
            sum1 += val
            sum2 -= val
            queue1.append(val)
        else:
            return cnt
    
    return -1