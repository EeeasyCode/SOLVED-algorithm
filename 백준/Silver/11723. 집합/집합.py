import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    menu = input().split()
    if len(menu) == 1:
        if menu[0] == 'all':
            for i in range(1, 21):
                S.add(i)
        else:
            S.clear()
    else:
        method = menu[0]
        k = int(menu[1])

        if method == 'add':
            S.add(k)

        elif method == 'remove':
            S.discard(k)

        elif method == 'check':
            if k in S:
                print(1)
            else:
                print(0)

        elif method == 'toggle':
            if k in S:
                S.discard(k)
            else:
                S.add(k)
