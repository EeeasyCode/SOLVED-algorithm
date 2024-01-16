def solution(array, commands):
    answer = []
    for command in commands:
        temp_arr = []
        i, j, k = command[0]-1, command[1]-1, command[2]-1
        temp_arr = array[i:j+1]
        temp_arr.sort()
        answer.append(temp_arr[k])
        
    return answer