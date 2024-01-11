def solution(board, moves):
    stack = [0] 
    cnt = 0
    for move in moves:
        for b in board:
            if b[move-1] != 0:
                if stack[-1] == b[move-1]:
                    stack.pop()
                    b[move-1] = 0
                    cnt += 2
                    break
                else:
                    stack.append(b[move-1])
                    b[move-1] = 0
                    break
    
    return cnt