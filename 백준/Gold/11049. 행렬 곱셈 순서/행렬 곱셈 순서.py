import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())

    nums = list(map(int, input().split()))
    for _ in range(N-1):
        _, c = map(int, input().split())
        nums.append(c)

    # DP
    dp = [[0]*N for _ in range(N)]
    for d in range(N):
        for i in range(N - d):
            j = i + d

            if i == j:
                continue

            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1]
                               [j] + nums[i]*nums[k+1]*nums[j+1])

    print(dp[0][-1])