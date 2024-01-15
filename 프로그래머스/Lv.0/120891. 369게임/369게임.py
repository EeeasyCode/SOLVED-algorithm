def solution(order):
    answer = 0
    for o in str(order):
         if int(o) == 3 or int(o) == 6 or int(o) == 9:
                answer += 1
    return answer