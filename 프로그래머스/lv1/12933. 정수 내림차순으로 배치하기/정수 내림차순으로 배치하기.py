def solution(n):
    answer = []
    key = ''
    for i in range(len(str(n))):
        answer.append(str(n)[i])
    answer.sort(reverse = True)
    key = ''.join(answer)
        
    return int(key)