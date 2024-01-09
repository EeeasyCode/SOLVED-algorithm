def solution(answers):
    answer = [0] * 3
    one_arr = [1,2,3,4,5]
    two_arr = [2,1,2,3,2,4,2,5]
    three_arr = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if (answers[i] == one_arr[i%len(one_arr)]):
            answer[0] += 1
        if (answers[i] == two_arr[i%len(two_arr)]):
            answer[1] += 1
        if (answers[i] == three_arr[i%len(three_arr)]):
            answer[2] += 1
    
    max_val = max(answer)
    high_score = []
    for i in range(len(answer)):
        if max_val == answer[i]:
            high_score.append(i+1)
    
    return sorted(high_score)