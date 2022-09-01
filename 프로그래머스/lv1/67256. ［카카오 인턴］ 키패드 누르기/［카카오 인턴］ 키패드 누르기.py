def solution(numbers, hand):
    answer = ''
    left_num = [1, 4, 7]
    right_num = [3, 6, 9]
    left_now = 10
    right_now = 12
    for i in range(len(numbers)):
        numbers[i]=11 if numbers[i]==0 else numbers[i]
        if (numbers[i] in left_num):
            answer += 'L'
            left_now = numbers[i]
        elif (numbers[i] in right_num):
            answer += 'R'
            right_now = numbers[i]
        else:
            if (sum(divmod(abs(numbers[i] - left_now),3)) > sum(divmod(abs(numbers[i] - right_now),3))):
                right_now = numbers[i]
                answer += 'R'
                
            elif (sum(divmod(abs(numbers[i] - left_now),3)) < sum(divmod(abs(numbers[i] - right_now),3))):
                left_now = numbers[i]
                answer += 'L'
            else:
                if (hand == "right"):
                    right_now = numbers[i]
                    answer += 'R'
                else:
                    left_now = numbers[i]
                    answer += 'L'
            
        
    return answer