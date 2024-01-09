def solution(N, stages):
    challenger = [0] * (N+2)
    
    for stage in stages:
        challenger[stage] += 1
    
    total = len(stages)
    fail_props = {}
    
    for i in range(1, N+1):
        if challenger[i] == 0:
            fail_props[i] = 0
        else:
            fail_props[i] = challenger[i] / total
            total -= challenger[i]
    result = sorted(fail_props, key=lambda x: fail_props[x], reverse=True)
    return result