def solution(prices):
    
    stack = [0] 
    n = len(prices)
    answer = [0] * n
    for i in range(1, n):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer