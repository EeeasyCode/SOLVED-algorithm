def solution(n):

    x = n ** (0.5)
    
    if x % 1 == 0:
        return (x+1) ** 2
    return -1