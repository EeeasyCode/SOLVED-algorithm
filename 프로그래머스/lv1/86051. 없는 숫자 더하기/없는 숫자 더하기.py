def solution(numbers):
    answer = 0
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for num in number_list:
        if num not in numbers:
            answer += num
            
    
    
    return answer