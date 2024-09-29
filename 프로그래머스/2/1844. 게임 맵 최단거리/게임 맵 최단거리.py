from collections import deque

def solution(maps):
    def bfs(x, y):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        queue = deque()
        queue.append((x, y))
        size = 1
        while queue:
            fx, fy = queue.popleft()
            for k in range(4):
                nx = fx + dx[k]
                ny = fy + dy[k]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[ny][nx] == 1 and check[ny][nx] == False:
                        check[ny][nx] = True
                        maps[ny][nx] = maps[fy][fx] + 1
                        queue.append((nx, ny))
        return size
    
    answer = 0
    n, m = len(maps[0]), len(maps)
    check = [[False] * n for _ in range(m)]
    min_dist = 9999
    check[0][0] = True
    

    bfs(0,0)
    answer = maps[-1][-1]
    
    if answer == 1:
        return -1
    else:
        return answer