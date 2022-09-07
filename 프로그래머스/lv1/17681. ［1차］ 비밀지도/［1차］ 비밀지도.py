def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i] | arr2[i])
        a = a[2:].zfill(n)
        a = a.replace('1', '#').replace('0', ' ')
        answer.append(a)
        
        
        
        
        
    
    
    
    return answer