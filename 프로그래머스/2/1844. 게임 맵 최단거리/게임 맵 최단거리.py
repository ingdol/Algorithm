from collections import deque
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(maps):
    row = len(maps[0])
    column = len(maps)
    visited = [[0 for _ in range(row)] for _ in range(column)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = 1
    
    while queue:
        cx, cy, cnt = queue.popleft()
        
        if cx == row -1 and cy == column -1:
            return cnt
        
        for x, y in direction:
            nx, ny = cx + x, cy + y
            if 0 <= nx < row and 0 <= ny < column and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                visited[ny][nx] = 1
                queue.append((nx, ny, cnt + 1))
    return -1

def solution(maps):
    return bfs(maps)
