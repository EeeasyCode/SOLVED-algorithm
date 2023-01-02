import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

p_arr = [0]
for i in arr:
  p_arr.append(p_arr[-1] + i)

for _ in range(m):
  a, b = map(int, input().split())
  print(p_arr[b] - p_arr[a - 1])
