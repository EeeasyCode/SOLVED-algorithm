from collections import deque

def solution(s):
    answer = True
    stack = deque()
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.popleft()
            else:
                return False
    
    
    if not stack:
        return True
    else:
        return False