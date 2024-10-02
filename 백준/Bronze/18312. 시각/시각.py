n, k = map(int, input().split())
k = str(k)
answer = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if len(str(h)) == 1:
                h = '0' + str(h)
            if len(str(m)) == 1:
                m = '0' + str(m)
            if len(str(s)) == 1:
                s = '0' + str(s)

            if  k in str(h) or k in str(m) or k in str(s):
                answer += 1

print(answer)
