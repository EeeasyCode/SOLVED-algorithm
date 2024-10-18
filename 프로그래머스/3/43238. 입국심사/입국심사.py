def solution(n, times):
    answer = 0
    start, end = 1, min(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        cnt = 0
        for time in times:
            cnt += mid // time
        
        if cnt < n:
            start = mid + 1
        else:
            end = mid - 1
    return start