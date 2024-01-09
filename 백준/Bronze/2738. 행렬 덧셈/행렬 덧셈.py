a_arr, b_arr = [], []
n, m = map(int, input().split())

for row in range(n):
  a_arr.append(list(map(int, input().split())))

for row in range(n):
  b_arr.append(list(map(int, input().split())))

for row in range(n):
  for col in range(m):
    print(a_arr[row][col]+b_arr[row][col], end=' ')
  print()