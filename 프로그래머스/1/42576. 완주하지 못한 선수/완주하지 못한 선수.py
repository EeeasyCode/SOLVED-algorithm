def solution(participant, completion):
    dict = {}
    
    for p in participant:
        if p in dict:
            dict[p] += 1
        else: 
            dict[p] = 1
    
    for c in completion:
        if c in dict.keys():
            dict[c] -= 1
    
    for k, v in dict.items():
        if v != 0:
            return k

    
    return dict
            
    
    
    