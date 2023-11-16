T = int(input())

for _ in range(T):
  N = int(input())
  zero_arr = [1, 0, 1]
  one_arr = [0, 1, 1]
  for i in range(2, N):
    zero_arr.append(zero_arr[i] + zero_arr[i-1])
    one_arr.append(one_arr[i] + one_arr[i-1])
  print(str(zero_arr[N]) + " " + str(one_arr[N]))