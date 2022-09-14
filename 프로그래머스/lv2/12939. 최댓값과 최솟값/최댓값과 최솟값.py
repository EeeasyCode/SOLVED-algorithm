def solution(s):
    answer = ''
    key = []
    max_num, min_num = 0, 0
    result = ""
    answer = s.split()
    for i in answer:
        key.append(int(i))
    
    max_num = max(key)
    min_num = min(key)
    
    answer = str(min_num) + ' ' + str(max_num)
        
    return answer