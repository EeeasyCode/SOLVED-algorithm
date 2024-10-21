def solution(x, n):
    answer = []
    answer.append(x)
    for i in range(1, n):
        answer.append(answer[i-1] + x)
    
    return answer