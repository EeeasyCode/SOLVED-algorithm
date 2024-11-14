import sys
input = sys.stdin.readline

N = int(input())

num_arr = []

for _ in range(N):
    x, y = map(int, input().split())
    num_arr.append([x, y])

num_arr = sorted(num_arr, key=lambda x: (x[1], x[0]))

for num in num_arr:
    print(f"{num[0]} {num[1]}")