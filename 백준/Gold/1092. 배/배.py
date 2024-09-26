N = int(input())
L = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
W = sorted(list(map(int, input().split())), reverse=True)

count = 0

if max(L) < max(W):
    print(-1)
else:
    while M != 0:
        count += 1
        for l in L:
            if M > 0 and l < W[-1]:
                continue
            for w in W:
                if w <= l:
                    W.remove(w)
                    M -= 1
                    break
    print(count)
