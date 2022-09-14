def solution(n):
    answer = ''
    su = '수'
    bak = '박'
    for i in range(n//2):
        answer += su
        answer += bak
    if (n%2!=0):
        answer += su
    
        
        
        
    return answer