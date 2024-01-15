def solution(num_list, n):
    answer = []
    temp_arr = []
    for num in num_list:
        temp_arr.append(num)
        if len(temp_arr) % n == 0:
            answer.append(temp_arr)
            temp_arr=[]
    return answer