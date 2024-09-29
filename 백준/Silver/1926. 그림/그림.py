from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
draw_map = [list(map(int, input().split())) for _ in range(n)]
check_map = [[False] * m for _ in range(n)]
draw_count = 0
max_size = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(y, x):
    size = 1
    bfs_queue = deque()
    bfs_queue.append((y, x))

    while bfs_queue:
        fy, fx = bfs_queue.popleft()
        for k in range(4):
            nx = fx + dx[k]
            ny = fy + dy[k]

            if 0 <= nx < m and 0 <= ny < n:
                if draw_map[ny][nx] == 1 and check_map[ny][nx] == False:
                    check_map[ny][nx] = True
                    size += 1
                    bfs_queue.append((ny, nx))
    return size

for j in range(n):
    for i in range(m):
        if draw_map[j][i] == 1 and check_map[j][i] == False:
            check_map[j][i] = True
            draw_count += 1
            max_size = max(max_size, bfs(j, i))

print(draw_count)
print(max_size)
