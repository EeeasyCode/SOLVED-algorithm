N = int(input())

min_b = 9999

for _ in range(N):
    a, b = map(int, input().split())
    if b < min_b:
        min_b = b
        answer = str(a) + ' ' + str(b)

print(answer)