def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0]-1, command[1], command[2]-1
        temp = []
        temp.append(array[i:j])
        temp[0].sort()
        answer.append(temp[0][k])
        
    return answer