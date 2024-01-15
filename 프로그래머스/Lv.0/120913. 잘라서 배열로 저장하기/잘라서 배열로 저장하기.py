def solution(my_str, n):
    answer = []
    temp_str = ''
    for i, c in enumerate(my_str):
        temp_str += c
        if (i+1)%n==0:
            answer.append(temp_str)
            temp_str=''
    if len(my_str) % n != 0:
        answer.append(temp_str)
    return answer