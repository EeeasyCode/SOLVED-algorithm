def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        array_index = []
        front = commands[i][0]
        rear = commands[i][1]
        index = commands[i][2]
        array_index = array[front-1:rear]
        array_index.sort()
        answer.append(array_index[index-1])
        print(array_index)
    return answer