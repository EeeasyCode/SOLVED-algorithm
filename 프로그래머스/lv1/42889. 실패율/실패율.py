def solution(N, stages):
    clients = len(stages)
    props = dict()
    
    for i in range(1, N+1):
        if clients != 0:
            cnt = stages.count(i)
            fail_props = cnt/clients
            props[i] = fail_props
            clients -= cnt
        else:
            props[i] = 0
    
    return sorted(props, key=lambda x:props[x], reverse=True)