def solution(n):
    answer = 0
    a, b = 1, 2
    if (n==a):
        return a
    for _ in range(2, n):
        a, b = b, a+b
        
    return b % 1234567