from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        count = 0
        if progresses[0] < 100:
            for i, _ in enumerate(progresses):
                progresses[i] += speeds[i]
        else:
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            answer.append(count)
    return answer