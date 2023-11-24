def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n - len(lost)
    return answer