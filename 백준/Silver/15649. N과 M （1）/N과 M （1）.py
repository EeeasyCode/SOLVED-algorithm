N, M = map(int, input().split())

answer = []
flag = [False] * (N+1)

def recur(num):
	if num == M:
		print(' '.join(map(str, answer)))
		return
	
	for i in range(1, N+1):
		if not flag[i]:
			flag[i] = True
			answer.append(i)
			recur(num+1)
			flag[i] = False
			answer.pop()

recur(0)