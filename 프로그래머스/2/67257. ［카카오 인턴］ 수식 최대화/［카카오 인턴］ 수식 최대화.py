from itertools import permutations
from re import split

def solution(expression):
    answer = []    
    for priority in permutations(['*', '-', '+'], 3):
        operands = list(map(int, split('[\*\+\-]', expression)))
        operators = [o for o in expression if o in '*+-']
        
        for op in priority:
            while op in operators:
                i = operators.index(op)
                
                if op == '*':
                    value = operands[i] * operands[i+1]
                elif op == '+':
                    value = operands[i] + operands[i+1]
                else:
                    value = operands[i] - operands[i+1]
                
                operands[i] = value
                operands.pop(i+1)
                operators.pop(i)
        answer.append(operands[0])
                
    max_val = max(abs(v) for v in answer)
    
        
    return max_val