N, X = map(int, input().split())

num_arr = map(int, input().split())

for num in num_arr:
  if num < X:
    print(num, end=' ')