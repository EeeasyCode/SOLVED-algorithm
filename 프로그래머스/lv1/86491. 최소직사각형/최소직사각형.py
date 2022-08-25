def solution(sizes):
    answer = 0
    w = []
    h = []
    
    for i in sizes:
        w.append(max(i)) 
        h.append(min(i))
    
    max_w = max(w)
    max_h = max(h)
    
    answer = max_w * max_h
    
    return answer