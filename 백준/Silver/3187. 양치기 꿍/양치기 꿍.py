import sys
input = sys.stdin.readline
from collections import deque

# BFS 함수 정의
def bfs(x, y):
    global sheep, wolf
    queue = deque([(x, y)])
    visited[x][y] = True
    
    # 양과 늑대 세기
    if field[x][y] == 'k':
        sheep += 1
    elif field[x][y] == 'v':
        wolf += 1

    # BFS 탐색
    while queue:
        cx, cy = queue.popleft()

        # 네 방향으로 탐색 (상, 하, 좌, 우)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            # 범위를 벗어나지 않고, 울타리가 아니며, 방문하지 않은 곳
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] != '#':
                visited[nx][ny] = True
                
                if field[nx][ny] == 'k':
                    sheep += 1
                elif field[nx][ny] == 'v':
                    wolf += 1

                queue.append((nx, ny))

# 입력 받기
R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
total_sheep, total_wolf = 0, 0

# 모든 위치를 탐색
for i in range(R):
    for j in range(C):
        if field[i][j] != '#' and not visited[i][j]:
            # 새로운 구역마다 양과 늑대 수 초기화
            sheep, wolf = 0, 0
            bfs(i, j)

            # 양의 수가 더 많으면 늑대가 전부 잡아먹힘
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

# 결과 출력
print(total_sheep, total_wolf)