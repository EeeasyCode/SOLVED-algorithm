def solution(i, j, k):
    answer = 0
    for s in range(i, j+1):
        for a in str(s):
            if int(a) == k:
                answer += 1
    return answer