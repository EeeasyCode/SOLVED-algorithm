def solution(progresses, speeds):
    answer = []
    a = []
    b = []
    for i in progresses:
        a.append(100 - i)
    
    for i in range(len(a)):
        if a[i] % speeds[i] == 0:
            b.append(a[i]//speeds[i])
        else:
            b.append(a[i]//speeds[i] + 1)
    
    max_i, i = b.pop(0), 1
    
    while b:
        k = b.pop(0)
        if max_i < k:
            answer.append(i)
            max_i = k
            i = 1
        else:
            i += 1
    answer.append(i)
    return answer