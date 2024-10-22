N, M = map(int, input().split())
bulb_list = list(map(int, input().split()))

for _ in range(M):
    c_n, a, b = map(int, input().split())
    
    if c_n == 1:
        bulb_list[a-1] = b
    elif c_n == 2:
        for i in range(a-1, b):
            if bulb_list[i] == 0:
                bulb_list[i] = 1
            else:
                bulb_list[i] = 0
    elif c_n == 3:
        for i in range(a-1, b):
            bulb_list[i] = 0
    else:
        for i in range(a-1, b):
            bulb_list[i] = 1

print(*bulb_list)