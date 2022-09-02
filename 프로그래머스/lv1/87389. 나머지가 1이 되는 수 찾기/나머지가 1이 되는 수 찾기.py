def solution(n):
    answer = 1
    flag = True
    while(flag):
        if n % answer == 1:
            flag = False
        else:
            answer += 1
    return answer