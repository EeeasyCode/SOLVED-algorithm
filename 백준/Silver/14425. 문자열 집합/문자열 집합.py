import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_dict = {}

for _ in range(n):
    n_str = input().rstrip()
    n_dict[n_str] = 1

answer = 0

for _ in range(m):
    f_str = input().rstrip()

    if f_str in n_dict.keys():
        answer += 1

print(answer)
