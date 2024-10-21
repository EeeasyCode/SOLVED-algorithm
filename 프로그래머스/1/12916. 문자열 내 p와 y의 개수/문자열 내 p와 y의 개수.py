def solution(s):
    answer = True
    
    a = s.upper()
    p_count = a.count('P')
    y_count = a.count('Y')
    
    if p_count == y_count:
        return True
    else:
        return False
    