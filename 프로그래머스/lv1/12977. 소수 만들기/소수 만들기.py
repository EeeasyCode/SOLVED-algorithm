from itertools import combinations
def is_prime_num(arr):
    if arr == 0 or arr == 1:
            return False
    else:
        for j in range(2, (arr//2)+1):
            if arr % j == 0:
                return False
        return True

def solution(nums):
    answer = 0
    
    nums_list = list(combinations(nums, 3))
    
    for i in nums_list:
        test = sum(i)
        if is_prime_num(test):
            answer += 1
                        
                    
        print(test)
    

    
                
    
    return answer