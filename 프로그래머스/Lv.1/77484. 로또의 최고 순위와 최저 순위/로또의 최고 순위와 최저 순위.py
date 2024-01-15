def solution(lottos, win_nums):
    best, worst = 0, 0
    best = lottos.count(0)
    while 0 in lottos:
        lottos.remove(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            best += 1
            worst += 1
    
    if not lottos:
        return [1, 6]
    
    if best==0 and worst ==0:
        return [6, 6]
    
    return [7-best, 7-worst]