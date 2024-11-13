import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    x, y = map(int, input().split())
    num_list.append([x, y])

num_list = sorted(num_list, key= lambda x: (x[0], x[-1]))

for x, y in num_list:
    print(x, y)