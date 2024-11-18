import sys
input = sys.stdin.readline

n = int(input())

rope_w = []

for _ in range(n):
    rope_w.append(int(input()))

rope_w.sort(reverse=True)

answer_list = []
answer_list.append(rope_w[0])

for i in range(1, len(rope_w)):
    answer_list.append(rope_w[i] * (i+1))

print(max(answer_list))
