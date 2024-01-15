def solution(num, total):
    answer = []
    index_num = total // num
    index_point = num // 2
    if num % 2 == 0:
        for i in range(index_num - index_point + 1, index_num + index_point + 1):
            answer.append(i)
    else:
        for i in range(index_num - index_point, index_num + index_point + 1):
            answer.append(i)
    return answer