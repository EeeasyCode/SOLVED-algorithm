n, m = map(int, input().split())
arr = list(map(int, input().split()))
p_arr = [0] * (n + 1)

for _ in range(m):
  a, b, k = map(int, input().split())
  p_arr[a - 1] += k
  p_arr[b] -= k

dp = [0] * (n + 1)
dp[0] = p_arr[0]
for i in range(1, n + 1):
  dp[i] = dp[i - 1] + p_arr[i]

for i in range(n):
  print(arr[i] + dp[i], end=' ')
