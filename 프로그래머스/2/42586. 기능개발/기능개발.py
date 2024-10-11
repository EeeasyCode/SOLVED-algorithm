import math
def solution(progresses, speeds):
    answer = []
    progress_left = []
    left_day = 0
    for i, progress in enumerate(progresses):
        left = 100 - progress
        progress_left.append(math.ceil(left/speeds[i]))
    
    max_day = progress_left[0]
    cnt = 0
    for i in range(len(progresses)):
        if progress_left[i] <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_day = progress_left[i]
    answer.append(cnt)
    return answer