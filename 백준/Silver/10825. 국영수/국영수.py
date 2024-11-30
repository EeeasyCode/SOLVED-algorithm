import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

# 이름 국어 영어 수학

score_list = []

for _ in range(n):
    score_list.append(input().split())

score_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for name in score_list:
    print(name[0])
