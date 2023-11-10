n = int(input())

dp = [0] * (n+1)
dp[0], dp[1] = 0, 1

for i in range(2, n):
  dp[i] = dp[i-1] + dp[i-2]

answer = dp[n-1] + dp[n-2] 

print(answer)