def solution(n):
    answer = ''
    
    while n > 0:
        n, m = divmod(n, 3)
        answer += str(m)
        print(n, m)
    answer = int(answer, 3)
    
    return answer