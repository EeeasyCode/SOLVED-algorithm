def solution(s):
    new_str = s[2:-2].split("},{")
    new_s = []
    for i in range(len(new_str)):
        s = new_str[i].split(",")
        new_s.append(set(s))
    
    
    new_s.sort(key=len)
    answer = set()
    k = []
    for i in new_s:
        tmp = i - answer
        k.append(list(tmp)[0])
        answer = answer | tmp
    
    an = []
    for i in k:
        an.append(int(i))
    
    
    return an