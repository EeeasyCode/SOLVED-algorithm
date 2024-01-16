def solution(s):
    answer = 0
    s_stack = []
    s_arr = s.split()
    for i in s_arr:
        if i == 'Z':
            s_stack.pop()
        elif i == ' ':
            continue
        else:
            s_stack.append(int(i))
    return sum(s_stack)