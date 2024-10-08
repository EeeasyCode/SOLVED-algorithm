import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 3]

if n==1:
    print(dp[0])
elif n==2:
    print(dp[1])
else:
    for i in range(2, n):
        dp.append((dp[i-1] + dp[i-2] * 2) % 10007)
    print(dp[n-1])