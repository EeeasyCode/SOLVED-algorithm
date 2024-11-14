import sys
input = sys.stdin.readline

N = list(map(int, str(input().rstrip())))

answer = sorted(N, reverse=True)

for ans in answer:
    print(ans, end='')
