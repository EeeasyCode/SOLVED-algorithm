k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    p, f = 1, 1
    for i in range(n):
        p *= m
        m -= 1
    for i in range(1, n+1):
        f *= i
    print(p//f)