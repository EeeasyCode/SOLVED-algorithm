import itertools
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    number_list = list(map(int, numbers))
    permu_list = []
    for i in range(1, len(numbers)+1):
        permu_list.append(list(map(''.join, (itertools.permutations(numbers, i)))))
    permu_list = list(set(map(int, sum(permu_list, []))))
    
    for num in permu_list:
        if is_prime(num):
            answer += 1
    
    return answer
