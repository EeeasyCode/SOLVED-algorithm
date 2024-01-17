def solution(participant, completion):
    answer = {}
    
    for part in participant: 
        if part in answer:
            answer[part] += 1
        else:
            answer[part] = 1
        
    for comp in completion:
        answer[comp] -= 1
    
    for k, v in answer.items():
        if v == 1:
            return k
    
    return 1
            
    
    
    