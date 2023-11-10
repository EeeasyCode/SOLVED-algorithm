def solution(board, moves):
    answer = 0
    stacks = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                stacks.append(board[j][i-1])
                board[j][i-1] = 0
                break;
        
        if len(stacks)>1:
            if stacks[-1] == stacks[-2]:
                del stacks[-1]
                del stacks[-1]
                answer += 2
        
    return answer