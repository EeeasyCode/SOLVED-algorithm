def solution(clothes):
    answer = 1
    dict = {}
    for clothe in clothes:
        c_name, c_type = clothe
        if c_type in dict:
            dict[c_type] += 1
        else:
            dict[c_type] = 1
    
    for v in dict.values():
        answer = answer * (v+1)
        
    return answer - 1