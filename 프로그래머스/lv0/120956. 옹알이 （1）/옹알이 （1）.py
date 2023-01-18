from itertools import permutations

def solution(babbling):
    answer = 0
    possible_list = ['aya', 'ye', 'woo', 'ma']
    possible_case = []
    for i in range(1, 5):
        for word in permutations(possible_list, i):
            possible_case.append(''.join(word))
    
    for word in babbling:
        if word in possible_case:
            answer += 1
    
    
            
        
        
        
                
    
    return answer