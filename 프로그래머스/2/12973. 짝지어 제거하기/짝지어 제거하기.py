def solution(s):
    answer = -1
    stack = []
    for c in s:
        if stack:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    if stack:
        return 0
    else:
        return 1

    return answer