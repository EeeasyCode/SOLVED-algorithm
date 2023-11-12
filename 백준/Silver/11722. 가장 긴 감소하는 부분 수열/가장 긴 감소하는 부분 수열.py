n = int(input())
a_arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
  for j in range(0, i):
    if a_arr[i] < a_arr[j]:
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))