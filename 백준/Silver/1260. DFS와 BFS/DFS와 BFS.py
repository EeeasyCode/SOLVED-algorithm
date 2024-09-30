import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

maps = [[0] * (N+1) for _ in range(N+1)]
visit_bfs = [0] * (N+1)
visit_dfs = [0] * (N+1)

for _ in range(M):
    y, x = map(int, input().split()) 
    maps[y][x] = 1
    maps[x][y] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(V):
    queue = deque()
    queue.append(V)
    visit_bfs[V] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if maps[i][v] == 1 and visit_bfs[i] == 0:
                queue.append(i)
                visit_bfs[i] = 1

def dfs(V):
    visit_dfs[V] = 1
    print(V, end=' ')            
    for i in range(1, N+1):
        if maps[i][V] == 1 and visit_dfs[i] == 0:
            dfs(i)      
        
dfs(V)
print()
bfs(V) 