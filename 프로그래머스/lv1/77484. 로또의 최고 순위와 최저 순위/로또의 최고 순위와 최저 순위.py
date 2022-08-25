def solution(lottos, win_nums):
    answer = []
    best = 0
    worst = 0
    
    best = lottos.count(0)
    while (0 in lottos):
        lottos.remove(0)
        
    for i in lottos:
        if i in win_nums:
            best += 1
            worst += 1
    
    answer = [7 - best, 7 - worst]
    if not lottos:
        answer = [1, 6]
    if (best == 0 and worst == 0):
        answer = [6, 6]
    return answer