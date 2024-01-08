n, m = map(int, input().split())

arr = [0] * n

for _ in range(m):
  a, b, c = map(int, input().split())
  for i in range(a-1, b):
    arr[i] = c

for i in arr:
  print(i, end=' ')