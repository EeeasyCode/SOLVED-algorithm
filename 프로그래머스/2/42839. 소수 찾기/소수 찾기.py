import itertools
def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    if numbers == '0' or numbers == '1':
        return 0
    int_arr = [num for num in numbers]
    num_arr = []
    for i in range(1, len(int_arr)+1):
        num_arr.append(list(set(map(''.join ,itertools.permutations(int_arr, i)))))
    
    num_arr = list(set(map(int, sum(num_arr, []))))
    
    for num in num_arr:
        if is_prime(num):
            answer += 1
            
    return answer