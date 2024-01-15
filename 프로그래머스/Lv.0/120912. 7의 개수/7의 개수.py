def solution(array):
    answer = 0
    for num in array:
        for c in str(num):
            if c == '7':
                answer += 1
    return answer