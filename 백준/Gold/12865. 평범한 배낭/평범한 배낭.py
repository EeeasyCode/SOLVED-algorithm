import sys
input = sys.stdin.readline

N, K = map(int, input().split())
w_list = [0]
v_list = [0]

for _ in range(N):
	W, V = map(int, input().split())
	w_list.append(W)
	v_list.append(V)

dp = [0] * (K+1)

for i in range(1, N+1):
	for k in range(K, w_list[i]-1, -1):
		if k >= w_list[i]:
			dp[k] = max(dp[k], dp[k-w_list[i]] + v_list[i])

print(dp[-1])