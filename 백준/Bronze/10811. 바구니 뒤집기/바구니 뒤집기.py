n, m = map(int, input().split())

arr = [0] * n

for i in range(n):
  arr[i] = i+1

for _ in range(m):
  a, b = map(int, input().split())
  arr[a-1:b] = arr[a-1:b][::-1]
  
for i in arr:
  print(i, end=' ')