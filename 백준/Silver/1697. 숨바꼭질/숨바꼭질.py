from collections import deque

N, K = map(int, input().split())

visit = [0 for _ in range(100001)]

def bfs(N):
    count = 0
    q = deque()
    q.append((N, count))

    while q:
        n, cnt = q.popleft()

        if n == K:
            return cnt
        
        if visit[n] == 0:
            cnt += 1
            visit[n] = 1

            if n + 1 < 100001:
                q.append((n+1, cnt))

            if 0 <= n - 1:
                q.append((n-1, cnt))
            
            if n * 2 < 100001:
                q.append((n*2, cnt))
    return count

print(bfs(N))
        
