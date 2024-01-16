def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            return False
                
    if stack:
        return False
    else:
        return True
    return True