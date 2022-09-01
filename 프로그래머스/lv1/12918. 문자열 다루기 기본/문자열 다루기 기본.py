def solution(s):
    answer = True
    
    if (len(s)== 4 or len(s) == 6):
        if s.isdigit():
            return True
        else:
            return False
    
    else:
        answer = False
        
    return answer