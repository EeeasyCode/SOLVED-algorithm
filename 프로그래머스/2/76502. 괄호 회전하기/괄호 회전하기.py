def check_str(s):
    stack = []
    for c in s:
        if (c=='(' or c=='{' or c=='['):
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif (c == ')' and stack[-1] == '('):
                stack.pop()
            elif (c == '}' and stack[-1] == '{'):
                stack.pop()
            elif (c == ']' and stack[-1] == '['):
                stack.pop()
    if stack:
        return False
    else:
        return True
    
def solution(s):
    check_status = check_str(s)
    total_cnt = 0
    if check_status:
        total_cnt += 1
    for i in range(len(s)-1):
        s = s[1:] + s[0]
        check_status = check_str(s)
        if check_status:
            total_cnt += 1
        
    return total_cnt