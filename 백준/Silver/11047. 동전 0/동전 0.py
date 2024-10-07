import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]
coin_list.reverse()
count = 0

for coin in coin_list:
	count += K // coin
	K %= coin

print(count)
